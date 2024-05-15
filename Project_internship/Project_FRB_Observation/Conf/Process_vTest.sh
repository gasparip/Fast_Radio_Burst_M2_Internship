#!/bin/sh
ls *.fits > NameFile.txt
mkdir SinglePulseFile
cat NameFile.txt | while  read file ; do
  directoryName=`echo $file| cut -d. -f1`
  mkdir $directoryName
  cp ./DDplan_NenuFAR_ModiftcpFRB2.py ./$directoryName
  mv $file $directoryName
  cd $directoryName
  csh -f `../FRB-search_PULSARmode_v2.csh $file 250 180 3 2.5 0.5 0.5` 
  cp *singlepulse.ps ../SinglePulseFile/
  cd ..
  echo $file >> ListFile2.5_3_0.5_0.5.txt
done


