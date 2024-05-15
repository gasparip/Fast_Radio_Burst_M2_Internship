#!/bin/bash
source /home/mbrionne/.mysetenv5_py2.bash
HighDm='240'
LowDm='200'
SigmaF='3'
SigmaT='3'
BerrF='0.5'
BerrT='0.5'
energy='100'
time='2000'
nameObs='sommes_TimeDiff100.fits'
dirName='sommes_TimeDiff100'
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f FRB20220912A_D20230604T0401_60099_253287_0054_BEAM1_0001.fits -o $nameObs -t 0 -e $energy -T 0.005
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f $nameObs -o 1$nameObs -t 1000 -e $energy -T 0.01
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 1$nameObs -o 2$nameObs -t 2000 -e $energy -T 0.015
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 2$nameObs -o 3$nameObs -t 3000 -e $energy -T 0.02
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 3$nameObs -o 4$nameObs -t 4000 -e $energy -T 0.03
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 4$nameObs -o 5$nameObs -t 5000 -e $energy -T 0.04
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 5$nameObs -o 6$nameObs -t 6000 -e $energy -T 0.05
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 6$nameObs -o 7$nameObs -t 7000 -e $energy -T 0.06
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 7$nameObs -o 8$nameObs -t 8000 -e $energy -T 0.07
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 8$nameObs -o 9$nameObs -t 9000 -e $energy -T 0.08
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 9$nameObs -o 10$nameObs -t 10000 -e $energy -T 0.09
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 10$nameObs -o 11$nameObs -t 11000 -e $energy -T 0.1
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 11$nameObs -o 12$nameObs -t 12000 -e $energy -T 0.5
python2.7 ../../../Script/CreateSimuAndPutInFits.py -f 12$nameObs -o 13$nameObs -t 13000 -e $energy -T 1
mkdir $dirName
mv 13$nameObs ./$dirName
rm *$nameObs
