#!/bin/bash

# Weekly Report Automation Script

## Overview

# This Bash script automates the generation of a weekly report for Nenufar observations in PULSAR and TF modes. 
# It compares the new observations with the previous week and generates a summary report in various formats, including PDFs and JPEGs.

## Usage

# 1. **Prerequisites:**
   # - Ensure that the required Python scripts (`pythonScriptAutomaticalSummarize.py` and `CreatePdf.py`) are available in the script's working directory.
   # - Set up the necessary environment using the provided `.mysetenv5_py2.bash` and `.mysetenv5_py3.bash` files.

# 2. **Configuration:**
   # - Update the email addresses in the `mailadresse` variable to receive the report.

# 3. **Execution:**
   # - Run the script using the command: `./ScriptAutomaticalSummarize.sh`

# Script Functionality

# - **Observation File Creation:**
  # - Generates lists of observation files for PULSAR and TF modes.

# - **Differential Analysis:**
  # - Compares the current week's observations with the previous week's records.
  # - Creates differential files for PULSAR and TF modes.

# - **Report Generation:**
  # - Checks for new observations and generates a summary report in a text file (`ForPDFtxt.txt`).

# - **PULSAR Mode Processing:**
  # - If new PULSAR observations are detected, executes Python scripts for further processing.
  # - Creates directories for data storage and generates JPEGs and PDFs from PULSAR data.

# - **TF Mode Processing:**
  # - If new TF observations are detected, processes the data and includes relevant information in the summary report.

# - **PDF Report Creation:**
  # - Creates a PDF report summarizing the weekly observations.

# - **Email Notification:**
  # - Sends an email with the generated PDF report attached to specified addresses.
  
  
current_date=$(date)
formatted_date=$(date +"%Y-%m-%d")
name_date=$(date +"%A")

ls /databf/nenufar-pulsar/??05/*/*/*.fits > /data/pgaspari/WeeklyReport/.processFile/NewDataBaseNenufarPulsarMode.txt
ls -d /databf/nenufar-tf/??05/*/*/* > /data/pgaspari/WeeklyReport/.processFile/NewDataBaseNenufarTfMode.txt

OldPulsarFile="/data/pgaspari/WeeklyReport/.processFile/OldDataBaseNenufarPulsarMode.txt"
NewPulsarFile="/data/pgaspari/WeeklyReport/.processFile/NewDataBaseNenufarPulsarMode.txt"
OldTfFile="/data/pgaspari/WeeklyReport/.processFile/OldDataBaseNenufarTfMode.txt"
NewTfFile="/data/pgaspari/WeeklyReport/.processFile/NewDataBaseNenufarTfMode.txt"
FpythonPulsarDiff="/data/pgaspari/WeeklyReport/.processFile/FpythonPulsarDiff.txt"
FpythonTfDiff="/data/pgaspari/WeeklyReport/.processFile/FpythonTfDiff.txt"
ToDoFile="/data/pgaspari/WeeklyReport/.processFile/ToDoFile.txt"
ForPDFtxt="/data/pgaspari/WeeklyReport/.processFile/ForPDFtxt.txt"
ForPythonToShToPDF="/data/WeeklyReport/BaseDonnee/.processFile/ForPythonToShToPDF.txt"

#put an email adress in this variable, you just need to add ,'youradress' in the str below
mailadresse="'pierregaspari@live.fr','cherrywyng@gmail.com','pierre.gaspari@cnrs-orleans.fr"

printf ""> $FpythonTfDiff
printf ""> $FpythonPulsarDiff
printf ""> $ToDoFile
printf ""> $ForPythonToShToPDF
echo "
Observation between the last friday and this friday in PULSAR and TF modes 
"> $ForPDFtxt
diff_output_Pulsar=$(diff "$OldPulsarFile" "$NewPulsarFile")
diff_output_Tf=$(diff "$OldTfFile" "$NewTfFile")

if [ -z "$diff_output_Pulsar" ]; then
  echo "There are no new observation in PULSAR Mode"
  echo "There are no new observation in PULSAR Mode
" >> $ForPDFtxt
  BoulPulsar=0
else
  echo "There are new observation(s) in PULSAR mode"
  echo "$diff_output_Pulsar" > diff_Pulsar.txt
  echo "There are "`cat diff_Pulsar.txt | grep -E '>' | wc -l` "new Observation(s) in PULSAR mode this week:
" >> $ForPDFtxt
  rm diff_Pulsar.txt
  BoulPulsar=1
  for lignePulsar in $diff_output_Pulsar
  do
  if [[ ${lignePulsar:0:1} == "/" ]] ; then
  	echo $lignePulsar | cut -d/ -f7 | cut -d_ -f1 >> $FpythonPulsarDiff
  	echo $lignePulsar | cut -d/ -f7 | cut -d_ -f2 | cut -dT -f1 | cut -dD -f2 >> $FpythonPulsarDiff
	echo $lignePulsar >> $FpythonPulsarDiff
	echo "	Obs Date : "`echo $lignePulsar | cut -d/ -f7 | cut -d_ -f2 | cut -dT -f1 | cut -dD -f2`"	Obs Name : "`echo $lignePulsar | cut -d/ -f7 | cut -d_ -f1` >> $ForPDFtxt
  fi
  done
fi

if [ -z "$diff_output_Tf" ]; then
  echo "There are no new observation in TF Mode"
  echo "
  
There are no new Observation in TF mode this week:
" >> $ForPDFtxt
  BoulTf=0
else
  echo "There are new observation in TF mode"
  echo "$diff_output_Tf" > diff_Tf.txt
  BoulTf=1
  echo "
  
There are "`cat diff_Tf.txt | grep -E '>' | wc -l` "new Observation(s) in TF mode this week:
" >> $ForPDFtxt
  rm diff_Tf.txt
  for ligneTf in $diff_output_Tf
  do
  if [[ ${ligneTf:0:1} == "/" ]] ; then
  	echo $ligneTf | cut -d/ -f7 | cut -d_ -f5 >> $FpythonTfDiff
  	echo $ligneTf | cut -d/ -f7 | cut -d_ -f1 >> $FpythonTfDiff
  	echo "	Obs Date : "`echo $ligneTf | cut -d/ -f7 | cut -d_ -f1`"	Obs Name : "`echo $ligneTf | cut -d/ -f7 | cut -d_ -f5` >> $ForPDFtxt
  fi
  done
fi

if [[ $BoulPulsar == 1 ]] ; 
then
	python3 ./pythonScriptAutomaticalSummarize.py
	source /home/mbrionne/.mysetenv5_py2.bash
	oldIFS=$IFS     # sauvegarde du séparateur de champ
	IFS=$'\n'
	mkdir /data/pgaspari/WeeklyReport/DataRow/$formatted_date
	mkdir /data/pgaspari/WeeklyReport/Result/$formatted_date
	mkdir /data/pgaspari/WeeklyReport/Result/$formatted_date/SinglePulseFile
	mkdir /data/pgaspari/WeeklyReport/Result/$formatted_date/JPEG
	mkdir /data/pgaspari/WeeklyReport/Result/$formatted_date/PDFfile
	mkdir /data/pgaspari/WeeklyReport/Result/$formatted_date/DOCFile
	for ligneToProccess in $(cat $ToDoFile)
	do
	   echo $ligneToProccess
	   FRBname=`echo $ligneToProccess | cut -d" " -f1`
	   Datename=`echo $ligneToProccess | cut -d" " -f2`
	   DM=`echo $ligneToProccess | cut -d" " -f3`
	   PathFile=`echo $ligneToProccess | cut -d" " -f4`
	   fitsName=`echo $ligneToProccess | cut -d" " -f4 | cut -d\/ -f7`
	   HighDm=`echo $ligneToProccess | cut -d" " -f5`
	   LowDm=`echo $ligneToProccess | cut -d" " -f6`
	   SigmaF=`echo $ligneToProccess | cut -d" " -f7`
	   SigmaT=`echo $ligneToProccess | cut -d" " -f8`
	   BerrF=`echo $ligneToProccess | cut -d" " -f9`
	   BerrT=`echo $ligneToProccess | cut -d" " -f10`
	   DirName=`echo $FRBname"_"$Datename"_"$SigmaF"_"$SigmaT`
	   echo $fitsName
	   mkdir `echo /data/pgaspari/WeeklyReport/DataRow/$formatted_date/$DirName`
	   ln -s $PathFile /data/pgaspari/WeeklyReport/DataRow/$formatted_date/$DirName
	   cp /data/pgaspari/WeeklyReport/PiplineScript/* /data/pgaspari/WeeklyReport/DataRow/$formatted_date/$DirName/
	   cd /data/pgaspari/WeeklyReport/DataRow/$formatted_date/$DirName
	   csh -f `./FRB-search_PULSARmode_v2.csh $fitsName $HighDm $LowDm $SigmaF $SigmaT $BerrF $BerrT`
	   fileNamePS=`echo $DirName"_singlepulse.ps"`
	   fileNameJPG=`echo $DirName"_singlepulse.jpg"`
	   mv *singlepulse.ps $fileNamePS  
	   gs -sDEVICE=jpeg -dJPEGQ=40 -dNOPAUSE -dBATCH -dSAFER -r300 -sOutputFile=$fileNameJPG $fileNamePS
	   mv $fileNamePS /data/pgaspari/WeeklyReport/Result/$formatted_date/SinglePulseFile
	   mv $fileNameJPG /data/pgaspari/WeeklyReport/Result/$formatted_date/JPEG
	   rm *dat
	   rm *DM*
	   rm *8bit*
	   rm *rfifind*
	   rm *.ddplan
	   cd /data/pgaspari/WeeklyReport/
	done
	source /home/mbrionne/.mysetenv5_py3.bash
	python3 ./CreatePdf.py $current_date $formatted_date
	libreoffice --headless --convert-to pdf /data/pgaspari/WeeklyReport/Result/$formatted_date/DOCFile/"Report_"$formatted_date".odt"
	rm /data/pgaspari/WeeklyReport/Result/$formatted_date/JPG/"cropped_"*
	mv ./"Report_"$formatted_date".pdf" /data/pgaspari/WeeklyReport/Result/$formatted_date/PDFfile/
	## decomment for automatic use
	#cp $NewPulsarFile > $OldPulsarFile
    #cp $NewTfFile > $OldTfFile
	echo 'FRB Weekly Report' | mail -s "Weekly Report" -A /data/pgaspari/WeeklyReport/Result/$formatted_date/PDFfile/Report_$formatted_date.pdf 'pierregaspari@live.fr','cherrywyng@gmail.com','pierre.gaspari@cnrs-orleans.fr'
else 
  if [[ $BoulPulsar == 0 ]] ;
  then
  echo "Pas d'observation à traiter"
  echo "

No Observation to treat this week
">> $ForPDFtxt
  fi
fi


#echo "FRB Nenufar Report" | mail -s 'test' -A ./Test/fichier20.pdf $mailadresse

##!/bin/bash

# Convertir le fichier texte en PDF en utilisant pandoc
#pandoc mon_fichier.txt -o mon_fichier.pdf
#xdg-open TestPdf.pdf 





#while true; do
#  read -p "Do you want to perform the next action? (yes/no): " choice
#  case "$choice" in
#    yes)
#      # Perform the next action here
#      echo "Next action executed!"
#      break
#      ;;
#    no)
#      echo "Next action skipped."
#      break
#      ;;
#    *)
#      echo "Invalid choice. Please enter 'yes' or 'no'."
#      ;;
#  esac
#done
