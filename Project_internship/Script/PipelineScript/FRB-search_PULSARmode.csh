#!/bin/tcsh  

set FILE=$1  #fits
set OUTPUT=`echo $FILE | awk -F'.fits' '{print $1}'`
set MaxDM = $2
rm cmd.log
touch cmd.log

#Convert to 8 bit and smooth bandpass
set FILE8b =  `echo $FILE | cut -d '.' -f1`_8bit.fits
python /home/lbondonneau/scripts/pav/psrfits_search/flat_bandpass_clean2.py -flat_per_block -mean_threshold 6 -j 8 -f $FILE -o $FILE8b -pscrunch -clean -subblock 0.5

#RFI find
echo "Runing RFI find"
rfifind -psrfits -noclip -blocks 1 -freqsig 3 -timesig 3 -chanfrac 0.3 -intfrac 0.3 -o $OUTPUT $FILE8b


#Plot dynamic spectrum
#python /home/lbondonneau/scripts/pav/psrfits_search/plot_dynspec.py -gui -f $FILE8b -df 1 -chan_threshold 3 -time_threshold 3 -ds 4 -dm 26.7

#prepare the .readfile file
readfile $FILE8b>$OUTPUT\_8bit.readfile
#Make DD plan
python /home/cng/Scripts/DDplan_NenuFAR.py  -k $OUTPUT\_rfifind.mask -m $MaxDM -o $OUTPUT $FILE8b

#predpsubband -- make time series
foreach LINE ("`cat $OUTPUT.ddplan`")
    set loDM = `echo $LINE | awk '{print $1}'`
    set dDM = `echo $LINE | awk '{print $2}'`
    set	dS = 8 #`echo $LINE | awk '{print $3}'` not sure why DDplan value seems too large
    set	nsub = `echo $LINE | awk '{print $4}'`
    set	nDM = `echo $LINE | awk '{print $5}'`
    echo prepsubband -psrfits -noclip -nobary -dmstep $dDM -downsamp $dS -lodm $loDM  -numdms $nDM -mask $OUTPUT\_rfifind.mask -o search $FILE8b>>cmd.log
    prepsubband -psrfits -noclip -nobary -dmstep $dDM -downsamp $dS -lodm $loDM  -numdms $nDM -mask $OUTPUT\_rfifind.mask -o $OUTPUT $FILE8b
end

#Single pulse search each time series (.dat) and make summary plot   
python /home/cng/Scripts/single_pulse_search.py --fast --nobadblocks *.dat
#Just make summary plot
#python /home/cng/Scripts/single_pulse_search.py --fast --nobadblocks *.singlepulse

#Make waterfall plot of a specific candidate/burst
#T = start time in sec
#t = duration in sec
#python /usr/lib/python2.7/dist-packages/presto/waterfaller.py -dm  26.72 -s 1024 -T 1340 -t 1 --show-ts --show-spec --maskfile=B0154+61_null_58576_rfi_rfifind.mask B0154+61_null_58576_pow.fil



