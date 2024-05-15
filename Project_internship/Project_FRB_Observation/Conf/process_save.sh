#!/bin/bash
Path='/data/pgaspari/FRBObservation'
PathDir=$Path/'FRB_SGR_obs_dir'
filePathName=$Path/'PathEdit.txt'
NameProcess='Process_3_3_0.5_0.5_20230407'
logProccess='log_'$NameProcess'.txt'
SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'

# Chemin du répertoire à vérifier/créer
source /home/mbrionne/.mysetenv5_py2.bash
mkdir $Path/$NameProcess
cd  $Path/$NameProcess ## Changer si pas utilisé dans mon répértoire
echo $NameProcess" SigmaF:"$SigmaF" SigmaT:"$SigmaT" BerrF:"$BerrF" BerrT:"$BerrT" ">$logProccess
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

# Utilisation de l'instruction case pour gérer les différentes options
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
        echo "Option invalide"
        # Code à exécuter pour une option invalide
        exit
        ;;
esac
  HighDM=$(( $DM + 20))
  LowDM=$(( $DM - 20))
  if [ -d "$PathDir/$obsName" ]; then
    echo "Know FRB"
  else
    # Créer le répertoire
    mkdir "$PathDir/$obsName"
    echo "Le répertoire \"$PathDir/$obsName\" a été créé."
  fi
  if [ -d "$PathDir/$obsName/$obsDate" ]; then
    echo "Know Obs"
  else
    # Créer le répertoire
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
  csh -f `./FRB-search_PULSARmode_vFRBObservation.csh $filename $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT "$PathDir/$obsName/$obsDate/$outputName/" $outputName`
  #mv Dir_singlepulsePlot $outputName"_singlepulse.ps"
  #mv *rfifind.ps $outputName"_rfifind.ps"
  mv Dir_singlepulsePlot $PathDir/$obsName/$obsDate/$outputName/
  mv *rfifind* $PathDir/$obsName/$obsDate/$outputName/$outputName"_rfifind"
  #mv $outputName"_rfifind.ps" $PathDir/$obsName/$obsDate/$outputName/
  #mv *.singlepulse $PathDir/$obsName/$obsDate/$outputName/Dir_Singlepulse/
  mv Dir_singlepulseFile $PathDir/$obsName/$obsDate/$outputName/
  echo "# DM  	SNR  	time 	Sampling	downfact" > $PathDir/$obsName/$obsDate/$outputName/$outputName"Classic_singlepulse.csv" 
  IFS=$'\n'
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


#mv $filefits ./$filename
#echo $filename>information.txt

#test
#PathDir='/data/pgaspari/FRBObservation/FRB_SGR_obs_dir'
#obsName='FRB151125'
#obsDate='D20230415T1001'
#outputName='FRB151125_D20230415T1001_Process_Test_20230630'

#echo "# DM  	SNR  	time 	Sampling	downfact" > $PathDir/$obsName/$obsDate/$outputName/$outputName"_singlepulse.csv" 
#cat $PathDir/$obsName/$obsDate/$outputName/Dir_Singlepulse/* >$PathDir/$obsName/$obsDate/$outputName/$outputName"_singlepulse_ALL.csv"
#IFS=$'\n'
#for file in $PathDir/$obsName/$obsDate/$outputName/Dir_Singlepulse/* ; do 
#echo $file
#tail -n +2 "$file"

#tail -n +2 "$file" > $PathDir/$obsName/$obsDate/$outputName/$outputName"_singlepulse.csv"; done >> $PathDir/$obsName/$obsDate/$outputName/$outputName"_singlepulse.csv"
#done >> $PathDir/$obsName/$obsDate/$outputName/$outputName"_singlepulse.csv"
#IFS=' '

