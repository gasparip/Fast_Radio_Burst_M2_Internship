#!/bin/bash
PathFile='/data/pgaspari/ParametreOptimisation/Dir_Simu_Fits/'
Name_Simu='13sommes_TimeDiff100'
filename="$PathFile$Name_Simu"
SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'
HighDM='240'
LowDM='200'
mkdir StudyBlockSize_$Name_Simu
cd StudyBlockSize_$Name_Simu
mkdir ./PlotDir
mkdir ./SinglePulseFile
mkdir ./RfifindDir
OldBlockSize=1
BlockSize=1
for ((i=1; i<=5; i++))
do
    OldBlockSize=$BlockSize
    echo "Valeur de l'entier : $BlockSize"
    mkdir ./SinglePulseFile/SinglePulse_Block_$BlockSize
    mkdir ./RfifindDir/Rfifind_Block_$BlockSize
    csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$filename.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
    mv *singlepulse.ps $Name_Simu"_Blocks_"$BlockSize"_singlepulse.ps"
    mv $Name_Simu"_Blocks_"$BlockSize"_singlepulse.ps" ./PlotDir/
    mv *.singlepulse ./SinglePulseFile/SinglePulse_Block_$BlockSize/
    mv *rfifind* ./RfifindDir/Rfifind_Block_$BlockSize/
    rm *dat
    rm *DM*
    rm *8bit*
    rm *.ddplan
    rm *rfifind*
    BlockSize=$(( $OldBlockSize * 2 ))
    # Faites vos opérations ici avec la variable $i
done
#csh -f `./FRB-search_PULSARmode_vFRBObservation.csh $filename $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
