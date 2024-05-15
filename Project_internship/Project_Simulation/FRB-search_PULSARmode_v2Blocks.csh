#!/bin/tcsh  

set FILE=$1  #fits
set OUTPUT=`echo $FILE | awk -F'.fits' '{print $1}' | cut -d\/ -f6`
set MaxDM = $2
set MinDM = $3
set Freqsig = $4
set Timesig = $5
set Chanfrac = $6
set Intfrac = $7
set BlockSize = $8
rm cmd.log
echo M $MaxDM m $MinDM F $Freqsig T $Timesig C $Chanfrac I $Intfrac B $BlockSize

echo $MaxDM $MinDM $Freqsig $Timesig $Chanfrac $Intfrac $BlockSize $FILE> cmd.log

#Convert to 8 bit and smooth bandpass
set FILE8b =  `echo "$OUTPUT"_8bit.fits`
python2.7 /home/lbondonneau/scripts/pav/psrfits_search/flat_bandpass_clean2.py -flat_per_block -mean_threshold 6 -j 8 -f $FILE -o $FILE8b -pscrunch -clean -subblock $BlockSize

#RFI find
echo "Runing RFI find" >> cmd.log
rfifind -psrfits -noclip -blocks 1 -freqsig $Freqsig -timesig $Timesig -ncpus 10 -chanfrac $Chanfrac -intfrac $Intfrac -o $OUTPUT $FILE8b

#Plot dynamic spectrum
#python /home/lbondonneau/scripts/pav/psrfits_search/plot_dynspec.py -gui -f $FILE8b -df 1 -chan_threshold 3 -time_threshold 3 -ds 4 -dm 26.7

#prepare the .readfile file
readfile $FILE8b>$OUTPUT\_8bit.readfile
#Make DD plan
python2.7 /data/pgaspari/ParametreOptimisation/Script/DDplan_NenuFAR_ModiftcpFRB2.py -c 10 -k $OUTPUT\_rfifind.mask -m $MaxDM -o $OUTPUT $FILE8b -min $MinDM

#predpsubband -- make time series
foreach LINE ("`cat $OUTPUT.ddplan`")
    set loDM = `echo $LINE | awk '{print $1}'`
    set dDM = `echo $LINE | awk '{print $2}'`
    set	dS = 1 #`echo $LINE | awk '{print $3}'` not sure why DDplan value seems too large
    set	nsub = 192 #`echo $LINE | awk '{print $4}'`
    set	nDM = `echo $LINE | awk '{print $5}'`
    echo prepsubband -psrfits -noclip -nobary -dmstep $dDM -downsamp $dS -lodm $loDM  -numdms $nDM -mask $OUTPUT\_rfifind.mask -o search $FILE8b>>cmd.log
    prepsubband -psrfits -noclip -nobary -dmstep $dDM -downsamp $dS -lodm $loDM -nsub $nsub -numdms $nDM -mask $OUTPUT\_rfifind.mask -o $OUTPUT $FILE8b -ncpus 10
end


#Single pulse search each time series (.dat) and make summary plot   
#python ../single_pulse_search_NenuFAR.py -o 20224 -n 5500 --fast --nobadblocks *$OUTPUT*.dat

single_pulse_search.py --fast --nobadblocks *$OUTPUT*.dat -m 300
#Just make summary plot
#python ../single_pulse_search_NenuFAR2.py -o 20224 -n 5500 --fast --nobadblocks *$OUTPUT*.singlepulse
#python /home/cng/Scripts/single_pulse_search.py --fast --nobadblocks *.singlepulse

#Make waterfall plot of a specific candidate/burst
#T = start time in sec
#t = duration in sec
#python /usr/lib/python2.7/dist-packages/presto/waterfaller.py -dm  26.72 -s 1024 -T 1340 -t 1 --show-ts --show-spec --maskfile=B0154+61_null_58576_rfi_rfifind.mask B0154+61_null_58576_pow.fil



