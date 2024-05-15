#!/bin/bash
source /home/mbrionne/.mysetenv5_py2.bash
filename='/data/pgaspari/Simulation/DirTestSimu/TestParametreSimulation/FRB20220912A_D20230408T0601_60042_252992_0054_BEAM1_0001.fits'
nameProcess='ProccessNewSimu16B'
mkdir $nameProcess
cd $nameProcess
HighDM='240'
LowDM='200'
SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'
BlockSize='16'
time='2000'
DM='218.9'
Duration='0.010'
DurationStr='0_010'
mkdir ./PlotDir
mkdir ./SinglePulseFile
mkdir ./RfifindDir 
mkdir ./textFile

energy='0.4'
energystr='0_4'

nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='6'
energystr='6'

nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='7'
energystr='7'

nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='8'
energystr='8'

nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='9'
energystr='9'

nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits



