#!/bin/bash
ProcessName='Process10_10_0.5_0.5'
filePathName=$ProcessName'File.txt'
mkdir $ProcessName
find /databf/nenufar-pulsar/??05/ -name SGR\*.fits > ./$ProcessName/$filePathName
find /databf/nenufar-pulsar/??05/ -name FRB\*.fits >> ./$ProcessName/$filePathName
#find /databf/nenufar-pulsar/??05/ -name FRB20181030\*.fits > $filePathName
Freqsig=$1
Timesig=$2
Chanfrac=$3
Intfrac=$4
mkdir $ProcessName/maskfile
cd $ProcessName
#printf > ./$ProcessName/FileToPlot.txt
cat $filePathName | while  read path ; do
	obsName=`echo $path| cut -d/ -f7 | cut -d_ -f1`
	obsDate=`echo $path| cut -d/ -f7 | cut -d_ -f2`
	outputName=$obsName"_"$obsDate
	rfifind -psrfits -noclip -blocks 1 -freqsig $Freqsig -timesig $Timesig -ncpus 10 -chanfrac $Chanfrac -intfrac $Intfrac -o $outputName $path
	maskfile=$outputName'_rfifind.mask'
	echo ObsName:$obsName ObsDate:$obsDate freqsig:$Freqsig timesig:$Timesig chanfrac:$Chanfrac intfrac:$Intfrac blocks:1 >./$outputName'_bad_column.txt'
	python2.7 ../ReadPrestoMask_v2.py -m $maskfile --fits $path -t -p | tail -n 1 >> ./$outputName'_bad_column.txt'
	mv *rfifind.mask ./maskfile
	mv *rfifind.ps ./maskfile
	rm *rfifind*
	cat ./$outputName'_bad_column.txt' >> ./FileToPlot.txt
done
#python2.7 PlotRfi.py ./$ProcessName/FileToPlot.txt 
