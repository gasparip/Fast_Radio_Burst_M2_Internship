
#!/bin/bash
source /home/mbrionne/.mysetenv5_py2.bash
filename='/data/pgaspari/Simulation/DirTestSimu/TestParametreSimulation/FRB20220912A_D20230408T0601_60042_252992_0054_BEAM1_0001.fits'
nameProcess='ProccessNewSimu16B_SizePulse'
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
mkdir ./PlotDir
mkdir ./SinglePulseFile
mkdir ./RfifindDir 
mkdir ./textFile
energy='2'
energystr='2'

Duration='0.0005'
DurationStr='0_0005'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.001'
DurationStr='0_001'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.0025'
DurationStr='0_0025'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.005'
DurationStr='0_005'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.01'
DurationStr='0_01'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.025'
DurationStr='0_025'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.05'
DurationStr='0_05'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.1'
DurationStr='0_1'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.25'
DurationStr='0_25'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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

Duration='0.5'
DurationStr='0_5'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/ParametreOptimisation/Script/FRB-search_PULSARmode_v2Blocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
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


