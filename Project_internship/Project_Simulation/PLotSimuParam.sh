#!/bin/bash
Mode=$1
echo $Mode
filePathName=TextFilePath.txt
fileToPython=FileToPython.txt
printf ''> $fileToPython
printf ''> $filePathName
if (( $Mode == 'Amplitude' )); then 
	find ./ -type d -name textFile | grep -v 'Test' | grep -v 'SizePulse' | grep 'ssNewSimu' > $filePathName
	cat $filePathName | while  read path ; do
	echo $path
	dirName=`echo $path`
	echo $dirName
	ls $path | while read fileText ;do 
	echo $fileText >> $fileToPython
	echo $fileText
	if [ -s "$dirName/$fileText" ]; then
  		echo "fichier non vide"
  		cat $dirName/$fileText >> $fileToPython
  	else
  		echo "fichier vide"
  		echo 'VIDE' >> $fileToPython
	fi
	#echo $filename
	done
	done
	

elif (( $Mode == 'Duration' )); then 
	echo 'on rentre'	
	find ./ -type d -name textFile | grep -v 'Test' | grep -v 'SizePulse' | grep '16NewSimu' > $filePathName
	cat $filePathName | while  read path ; do
	echo $path
	dirName=`echo $path`
	echo $dirName
	ls $path | while read fileText ;do 
	echo $fileText >> $fileToPython
	echo $fileText
	if [ -s "$dirName/$fileText" ]; then
  		echo "fichier non vide"
  		cat $dirName/$fileText >> $fileToPython
  	else
  		echo "fichier vide"
  		echo 'VIDE' >> $fileToPython
	fi
	#echo $filename
	done
	done
fi
