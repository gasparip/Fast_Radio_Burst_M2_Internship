#!/bin/bash
ProcessNameDirFRB='Process_3_3_0\.5_0\.5_20230407'
ProcessName='Process_3_3_0\.5_0\.5_20230407_FRB_Pipeline'
filePathName=$ProcessName'File.txt'
find /data/pgaspari/FRBObservation/FRB_SGR_obs_dir/ -name *$ProcessNameDirFRB"_rfifind" -type d > $filePathName
mkdir $ProcessName
#find /databf/nenufar-pulsar/??05/ -name SGR\*.fits > ./$ProcessName/$filePathName
#find /databf/nenufar-pulsar/??05/ -name FRB\*.fits >> ./$ProcessName/$filePathName
#find /databf/nenufar-pulsar/??05/ -name FRB20181030\*.fits > $filePathName
Freqsig=$1
Timesig=$2
Chanfrac=$3
Intfrac=$4
Blocks=$5
mkdir $ProcessName/maskfile
cd $ProcessName
mv ../$filePathName ./
#printf > ./$ProcessName/FileToPlot.txt
cat $filePathName | while  read path ; do
	obsName=`echo $path| cut -d/ -f6`
	obsDate=`echo $path| cut -d/ -f7`
	pathObs=`find /databf/nenufar-pulsar/??05/* -name $obsName*$obsDate*.fits`
	outputName=$obsName"_"$obsDate
	#maskfile=`ls $path/*_rfifind.mask`
	cp $path/*rfifind.mask ./$obsName"_"$obsDate"_rfifind.mask"
	cp $path/*rfifind.inf ./$obsName"_"$obsDate"_rfifind.inf" # car . dans le nom de fichier
	cp $path/*rfifind.ps ./maskfile/$obsName"_"$obsDate"_rfifind.ps"
	maskfile=''$obsName"_"$obsDate"_rfifind.mask"
	echo ObsName:$obsName ObsDate:$obsDate freqsig:$Freqsig timesig:$Timesig chanfrac:$Chanfrac intfrac:$Intfrac blocks:$Blocks >./$outputName'_bad_column.txt'
	python2.7 ../ReadPrestoMask_v2.py -m $maskfile --fits $pathObs -t | tail -n 1 >> ./$outputName'_bad_column.txt'
	rm *rfifind*
	cat ./$outputName'_bad_column.txt' >> ./FileToPlot.txt
done
#python2.7 PlotRfi.py ./$ProcessName/FileToPlot.txt 
