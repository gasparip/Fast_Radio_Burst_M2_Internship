#!/bin/bash
source /home/mbrionne/.mysetenv5_py2.bash
filename='/data/pgaspari/Simulation/DirTestSimu/TestParametreSimulation/FRB20220912A_D20230408T0601_60042_252992_0054_BEAM1_0001.fits'
nameProcess='ProccessSinglePulseSearchSimu_B16'
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
Duration='0.002'
DurationStr='0_002'


energy='1'
energystr='1'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFitsV2.py -f $filename -o "$nameObs.fits" -t $time -e $energy -pd $Duration -dm $DM
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2SinglepulseSearchBLocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
SinglpulseParameter='1'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='2'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='3'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='4'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='6'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='9'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='14'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='20'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='30'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='45'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='70'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='100'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='150'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='220'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter='300'
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='10'
energystr='10'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFits.py -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2SinglepulseSearchBLocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
SinglpulseParameter=1
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=2
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=3
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=4
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=6
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=9
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=14
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=20
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=30
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=45
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=70
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=100
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=150
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=220
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=300
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits

energy='0.5'
energystr='0_5'
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize
echo -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
echo "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize
python2.7 /data/pgaspari/Simulation/Script/CreateSimuAndPutInFits.py -f $filename -o "$nameObs.fits" -t $time -e $energy -T $Duration
csh -f `/data/pgaspari/Simulation/Script/FRB-search_PULSARmode_v2SinglepulseSearchBLocks.csh "$nameObs.fits" $HighDM $LowDM $SigmaF $SigmaT $BerrF $BerrT $BlockSize`
mkdir ./RfifindDir/$nameObs"_rfifind"
mv *rfifind* ./RfifindDir/$nameObs"_rfifind"
SinglpulseParameter=1
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=2
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=3
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=4
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=6
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=9
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=14
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=20
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=30
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=45
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=70
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=100
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=150
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=220
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
SinglpulseParameter=300
single_pulse_search.py --fast --nobadblocks *.dat -m $SinglpulseParameter
nameObs='Simulation_E_'$energystr'_D_'$DurationStr'_B_'$BlockSize'_M_'$SinglpulseParameter
mkdir ./SinglePulseFile/$nameObs"_singlepulse"
mv *singlepulse.ps $nameObs"_singlepulse.ps"
mv $nameObs"_singlepulse.ps" ./PlotDir/
cat *singlepulse | sort -k 2 | grep -v DM | grep ' 2000\.' | tail -n1 > ./textFile/$nameObs".txt"
mv *.singlepulse ./SinglePulseFile/$nameObs"_singlepulse"
rm *dat
rm *DM*
rm *8bit*
rm *.ddplan
rm *rfifind*
rm *.fits



