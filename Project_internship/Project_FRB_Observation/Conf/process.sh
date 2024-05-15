#!/bin/bash

# This Bash script automates the processing of Fast Radio Burst from NenuFAR(FRB) observations.
# It sets up parameters, organizes directories, and iterates through a list of observations.
# For each observation, it extracts information, determines dispersion measures, runs a processing script, and organizes the output.
# The script is designed for flexibility, allowing customization based on specific observations and parameters.
# It logs details of the process and ensures a systematic and organized approach to handling FRB data.

# The script performs the following tasks:

## Parameter Setup:
# Defines paths and parameters for processing FRB observations, including file paths, process names, and parameter values.

## Environment Configuration:
# Sets up the environment by sourcing a configuration file (Marc Brionne parameter for this code).

## Directory and File Management:
# Creates a directory for the current processing session.
# Copies necessary configuration files for the observation processing.

## Observation Processing Loop:
# Reads observation paths from a file and processes each observation individually.
# Extracts relevant information (e.g., observation name, date) from the paths.
# Determines the Dispersion Measure (DM) based on the observation name using a case statement.
# Creates and organizes directories for FRB names and observation dates.
# Runs a C shell script (FRB-search_PULSARmode_vFRBObservation.csh) for each observation with specified parameters.
# Moves processed files to appropriate directories.

## Cleanup:
# Removes unnecessary files generated during the processing.

## Logging:
# Records details of the processing, including parameters used for each observation, in a log file.

## Note:
# The script assumes a specific directory structure and file locations, and it might be tailored to a particular data setup or processing pipeline.
# Customization is recommended based on the user's data and directory structure.

####### Select the various parameters below to run the process on all observations ######

#Parameter for saving treatment

Path='/data/pgaspari/FRBObservation' 
PathDir=$Path/'FRB_SGR_obs_dir'
filePathName=$Path/'PathEdit.txt' #File with all the links to the FRB .ps data to be processed
NameProcess='Process_3_3_0.5_0.5_B_8_20231307'
logProccess='log_'$NameProcess'.txt'

#Parameters for processing observations

SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'
BlockSize='8'

#Put in the right source that works with the treatment

source /home/mbrionne/.mysetenv5_py2.bash

## Processing part 

# Set up the different algorithms and versions to be used for processing

mkdir $Path/$NameProcess
cd  $Path/$NameProcess 
echo $NameProcess" SigmaF:"$SigmaF" SigmaT:"$SigmaT" BerrF:"$BerrF" BerrT:"$BerrT" Block:"$BlockSize>$logProccess
cp $Path/Conf/FRB-search_PULSARmode_vFRBObservation.csh ./
cp $Path/Conf/single_pulse_search_NenuFAR.py ./ 
cp $Path/Conf/DDplan_NenuFAR_ModiftcpFRB2.py ./
cat $filePathName | while  read path ; do
  echo $path
  ln -s $path ./
  filename=`echo $path| cut -d/ -f7`
  obsName=`echo $path| cut -d/ -f7 | cut -d_ -f1`
  obsDate=`echo $path| cut -d/ -f7 | cut -d_ -f2`
  outputName=$obsName"_"$obsDate"_"$NameProcess
  DM=0


case "$obsName" in
    FRB20180916B|FRB180916)
        DM=349
        ;;
    FRB20200120E|FRB200120)
        DM=87
        ;;
    FRB20181030A|FRB181030)
        DM=103
        ;;
    FRB20180814A|FRB180814)
        DM=189
        ;;
    FRB20180908B|FRB180908)
    	DM=195
        ;;
    FRB20220912A)
        DM=218
        ;;
    FRB20190303A|FRB190303)
        DM=221
        ;;
    FRB20181017A|FRB181017)
        DM=239
        ;;
    FRB151125)
        DM=273
        ;;
    FRB190907)
        DM=310
        ;;
    SGR1935+2154)
        DM=332
        ;;
    FRB20121102A|FRB121102)
        DM=564
        ;;
    FRB20190425A|FRB190425)
        DM=128
        ;;
    FRB20181223C|FRB181223)
        DM=112
        ;;
    *)
        echo "invalid option"
        exit
        ;;
esac
 
 #DM window to display the DM vs Time plot diagram
  HighDM=$(( $DM + 20)) 
  LowDM=$(( $DM - 20))
 
 
  #Set up the FRB backup directories

  if [ -d "$PathDir/$obsName" ]; then
    echo "Know FRB"
  else
    # If it does not exist, create the directory
    mkdir "$PathDir/$obsName"
    echo "Le répertoire \"$PathDir/$obsName\" a été créé."
  fi
  if [ -d "$PathDir/$obsName/$obsDate" ]; then
    echo "Know Obs"
  else
    # If it does not exist, create the directory
    mkdir "$PathDir/$obsName/$obsDate"
    echo "Le répertoire \"$PathDir/$obsName/$obsDate\" a été créé."
  fi
  if [ -d "$PathDir/$obsName/$obsDate/$outputName" ]; then
    echo "Dir_OK"
  else 
    mkdir "$PathDir/$obsName/$obsDate/$outputName"
    mkdir $PathDir/$obsName/$obsDate/$outputName/$outputName"_rfifind"
    #mkdir "$PathDir/$obsName/$obsDate/$outputName/Dir_Singlepulse"
  fi
  
  # Proccessing section
  
  csh -f `./FRB-search_PULSARmode_vFRBObservation.csh $filename $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize $outputName`
  
  # Save results and clean unwanted files
  
  #mv Dir_singlepulsePlot $outputName"_singlepulse.ps"
  #mv *rfifind.ps $outputName"_rfifind.ps"
  mv Dir_singlepulsePlot $PathDir/$obsName/$obsDate/$outputName/
  mv *rfifind* $PathDir/$obsName/$obsDate/$outputName/$outputName"_rfifind"
  #mv $outputName"_rfifind.ps" $PathDir/$obsName/$obsDate/$outputName/
  #mv *.singlepulse $PathDir/$obsName/$obsDate/$outputName/Dir_Singlepulse/
  mv Dir_singlepulseFile $PathDir/$obsName/$obsDate/$outputName/
  echo "# DM  	SNR  	time 	Sampling	downfact" > $PathDir/$obsName/$obsDate/$outputName/$outputName"Classic_singlepulse.csv" 
  IFS=$'\n'
  # create the csv for the deep learning algorithm
  for file in $PathDir/$obsName/$obsDate/$outputName/Dir_singlepulseFile/single_pulse_search_fast/* ; do 
  tail -n +2 "$file"
  done >> $PathDir/$obsName/$obsDate/$outputName/$outputName"Classic_singlepulse.csv"
  echo "# DM  	SNR  	time 	Sampling	downfact" > $PathDir/$obsName/$obsDate/$outputName/$outputName"Nenufar_singlepulse.csv" 
  IFS=$'\n'
  for file in $PathDir/$obsName/$obsDate/$outputName/Dir_singlepulseFile/single_pulse_search_NenuFAR_fast/* ; do 
  tail -n +2 "$file"
  done >> $PathDir/$obsName/$obsDate/$outputName/$outputName"Nenufar_singlepulse.csv"
  IFS=' '
  rm *dat
  rm *DM*
  rm *8bit*
  rm *rfifind*
  rm *.ddplan
  echo $outputName >> $logProccess
done
