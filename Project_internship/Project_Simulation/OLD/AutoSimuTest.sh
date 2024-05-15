#!/bin/bash
source /home/mbrionne/.mysetenv5_py2.bash
cd /data/pgaspari/Simulation/DirTestSimu/
filename=$1
name=`echo $1 | cut -d/ -f7`
NbrDeTest=$2
NameSession=$3
HighDm='370'
LowDm='330'
SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'
energy=1
mkdir $NameSession
cd /data/pgaspari/Simulation/DirTestSimu/$NameSession
mkdir SinglePulseFile
cp /data/pgaspari/Simulation/Script/DDplan_NenuFAR_ModiftcpFRB2.py /data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2.csh ./
ln -s $filename ./
for ((i=1; i<=$NbrDeTest; i++))
do
    echo Test n° $i
    ThisTestName=$NameSession"_numero_"$i"_energy_$energy.fits"
    echo $name
    python2.7 /data/pgaspari/Simulation/Script/DoSimulationInFits.py -f $name -o $ThisTestName -e $energy
    NewEnergy=$((energy * 10))
    echo $NewEnergy
    energy=$NewEnergy
    csh -f `./FRB-search_PULSARmode_v2.csh $ThisTestName $HighDm $LowDm $SigmaF $SigmaT $BerrF $BerrT`
    ./data/pgaspari/GestionFileScript/Delete.sh
    mv *singlepulse.ps ./SinglePulseFile
done

