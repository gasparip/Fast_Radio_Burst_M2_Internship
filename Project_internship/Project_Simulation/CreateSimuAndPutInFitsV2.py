# -*- coding: utf-8 -*-
import numpy as np
import psrchive as psr
import pyfits as fi
import psrfits as pf
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import argparse as arg

## Observation 
parser = arg.ArgumentParser(description='Create a FRB Simulation and Put this one in a file')

parser.add_argument('-f', dest='fileName', type=str, help='Name of the FITS file to change.')
parser.add_argument('-o', dest='newFileName', type=str, help='Name of the new FITS file to write.')
parser.add_argument('-p', dest='plot', action='store_true', default=False, help="Plot the output file")
parser.add_argument('-e', dest='SignalEnergy', type=float, default=10.0, help='Change the energy value of the pulse simulation(default threshold = 10).')
parser.add_argument('-t', dest='TimePulse', type=float, default=200.0, help='Change the Time value of the pulse simulation(default threshold = 20s).')
parser.add_argument('-pd', dest='PulseDuration', type=float, default=0.100, help='Change the Duration of the pulse')
parser.add_argument('-dm', dest='DM', type=float, default=218.9, help='Change the DM value')
parser.add_argument('-s', dest='ScatteringMeasure', type=float, default=0.00105, help='Change the Scattering measure at 600Mhz value')
args = parser.parse_args()

obs = True
DocumentName=args.fileName #INPUT file
filename=args.newFileName #OUTPUT file

fi.info(DocumentName)
FileFits = pf.Arch(DocumentName)
FileFits.Dyn_spec_structure()
ArrayTF = FileFits.data
ListF=np.linspace(FileFits.lofreq,FileFits.hifreq,len(ArrayTF[0]))
ListT=np.linspace(0,FileFits.Tobs,len(ArrayTF[:,0]))
TimeFRB=float(args.TimePulse)
PulseDuration=float(args.PulseDuration)
if args.plot : 
	fig,axs = plt.subplots(2,2)
	TempsAmplobs = []
	#TempsAmplNorm =[]
	for j in range(len(ListT)):
		TempsAmplobs+=[sum(ArrayTF[j,:])/float(len(ArrayTF[j,:]))]
		#TempsAmplNorm +=[



	h=axs[1,0].pcolormesh(ListT, ListF ,ArrayTF.T)
	axs[1,0].set_xlabel('Temps(s)',fontsize = 15)
	axs[1,0].set_ylabel('Frequence(MHz)',fontsize = 15)
	#axs[0,0].colorbar()

	axs[0,0].plot(ListT,TempsAmplobs)
	axs[0,0].set_ylabel('Amplitude',fontsize = 15)
	axs[0,0].grid()
	#axs[0,0].colorbar()


## Parametre Simulation
if obs:
	TempsMax=1000
	ChanelFreq = FileFits.nchan
	Ds= float(FileFits.tsample)
	ChanelTemp=int(TempsMax/Ds)
	#DM=348.8 #FRB20180916B
	#DM=218.9 #FRB20220912A
	DM=float(args.DM)
	ScatteringMeasue=float(args.ScatteringMeasure)
	energyPulse= float(args.SignalEnergy)
	frequencyStart = float(FileFits.lofreq)	
	frequencyEnd = float(FileFits.hifreq)
	bw= FileFits.bw
	print(frequencyStart,frequencyEnd,Ds)
## Simulation

def FrenquencyBand(Fs,Fe,Fc):
	ListX = np.linspace(Fs,Fe,Fc)
	alpha = -1
	beta = Fs+Fe
	gama = -(alpha*Fs*Fs + beta*Fs)
	Y = alpha*ListX*ListX + beta*ListX + gama
	Y =Y/float(max(Y))
	return Y
	
def soustraire_liste(liste, nombre):
    resultat = []
    for element in liste:
        resultat.append(element - nombre)
    return resultat

def add_list(liste, nombre):
    resultat = []
    for element in liste:
        resultat.append(element + nombre)
    return resultat
	
ScatteringMode=True
Polynome = True

frequencyListCent = np.linspace(frequencyStart,frequencyEnd,ChanelFreq)
if Polynome : AmpliBandFreq = FrenquencyBand(frequencyStart,frequencyEnd,ChanelFreq)
ListTdm=[]
for i in range(ChanelFreq):
	ListTdm+=[DM*4.15e3*(1/float((frequencyListCent[i]**2)))]
print(ListTdm)
print(frequencyListCent)
ListTdm=soustraire_liste(ListTdm,ListTdm[-1]) ## Remettre la FRB Simuler à zéros.
#ListTdm=add_list(ListTdm,float(TimeFRB))
time=np.arange(0,TempsMax,Ds)
TimeFrequency = np.zeros((ChanelFreq,len(time)))
#time = np.linspace(0,TempsMax,ChanelTemp)

if ScatteringMode : timeConvolve=np.arange(-300,300,Ds)
for i in range(len(ListTdm)):
	#if Polynome : 
	#	energyPulseFreq = energyPulse*AmpliBandFreq[i]
	#	g1 = models.Gaussian1D(energyPulseFreq, ListTdm[i], PulseDuration)
	#else: 
	g1 = models.Gaussian1D(energyPulse, ListTdm[i], PulseDuration) # add more model if you want an other pulse
	signalFi = g1(time)
	
	if ScatteringMode :
		Tau=ScatteringMeasue*(600/float(frequencyListCent[i]))**(4)
		Courbscatt = np.zeros(len(timeConvolve))
		#print(Tau)
		for indice in range(len(timeConvolve)):
			if timeConvolve[indice] >= 0:
				Courbscatt[indice] = np.exp(-1*timeConvolve[indice]/float(Tau))/float(Tau)
				#Courbscatt[indice] = np.exp(-1*timeConvolve[indice]/float(Tau))
				
		Signal=(np.convolve(Courbscatt,signalFi,mode='same'))
	else : 
		
		if Polynome:
			Signal=signalFi * AmpliBandFreq[i]
		else:
			Signal=signalFi
	TimeFrequency[i] = Signal
if ScatteringMode:
	maxTimeFrequencyCen=max(TimeFrequency[int(float(ChanelFreq)/2)])
	sumEnergie=sum(TimeFrequency[int(ChanelFreq/2)]*energyPulse/float(maxTimeFrequencyCen))
	print(max(TimeFrequency[int(ChanelFreq/2)]*energyPulse/float(maxTimeFrequencyCen)))
	#maxValue=maxTimeFrequencyCen
	indexMax=int(ChanelFreq/2)
	maxValue=0
	for j in range(ChanelFreq):
		if max(TimeFrequency[j]) != 0 :
			TimeFrequency[j]= TimeFrequency[j]*sumEnergie/float(sum(TimeFrequency[j])) # Normalize each channel ( Energy Cst)
			if Polynome : TimeFrequency[j] = TimeFrequency[j]*AmpliBandFreq[j]
			maxChannel =  max(TimeFrequency[j])
			if maxChannel > maxValue:
				maxValue=maxChannel
				print(maxValue)
	for j in range(ChanelFreq):
		TimeFrequency[j] = TimeFrequency[j] * energyPulse/float(maxValue)  # Put the Maximum at the value that we want
		print(j,max(TimeFrequency[j]))
print(len(TimeFrequency.T))
print(int(TimeFRB/Ds))
print(len(ArrayTF))
print(len(ArrayTF[0]))
if (int(TimeFRB/Ds) + len(TimeFrequency.T)) > len(ArrayTF):
	tailleMax= len(ArrayTF) - int(TimeFRB/Ds)
	ArrayTF[:][int(TimeFRB/Ds):]=ArrayTF[:][int(TimeFRB/Ds):]+TimeFrequency.T[:][:tailleMax]
	#SNR = 
	print(1)
else:
	print(2)
	ArrayTF[:][int(TimeFRB/Ds):(int(TimeFRB/Ds)+len(TimeFrequency.T))]=ArrayTF[:][int(TimeFRB/Ds):(int(TimeFRB/Ds)+len(TimeFrequency.T))]+TimeFrequency.T
print(len(ArrayTF[:][int(TimeFRB/Ds):(int(TimeFRB/Ds)+len(TimeFrequency.T))]))
print(len(TimeFrequency.T))
print(int(TimeFRB/Ds)+len(TimeFrequency.T))
#ArrayTF[:][:71525]=ArrayTF[:][:71525]+TimeFrequency.T
#print(FileFits.data.shape)
FileFits.data=ArrayTF
FileFits.Subint_struct()

NewArray=[]
NewArray = np.swapaxes(FileFits.data,1,2)
data = fi.getdata(DocumentName)
print(data.shape)
dataArray=data.field(16)
dataCol=data.columns[16].copy()  
dataArray[:,:,0,:,0]=NewArray
colList = []        

        # Field list for the new fits file
for i in range(16):
	oldArray = data.field(i)                   # Copy of the old amplitude data array
	oldCol = data.columns[i].copy() 
	newCol = fi.Column(name=oldCol.name,         # Creation of the new field
		format=oldCol.format,
		unit=oldCol.unit,
		dim=oldCol.dim,
		array=oldArray)    
	colList.append(newCol)

newCol = fi.Column(name=dataCol.name,         # Creation of the new field
		format=dataCol.format,
		unit=dataCol.unit,
		dim=dataCol.dim,
		array=dataArray)    
colList.append(newCol)

headObs = fi.getheader(DocumentName, 0, do_not_scale_image_data=True, scale_back=True)        
head = fi.getheader(DocumentName, 1, do_not_scale_image_data=True, scale_back=True) 


colDefs = fi.ColDefs(colList)                    # Creation of the new fields object
tbhdu = fi.BinTableHDU.from_columns(colDefs, header=head)    # Creation of the new data table object

prihdu = fi.PrimaryHDU(header=headObs)            # Creation of the new observation header (exactly the same that the old fits file)
hdulist = fi.HDUList([prihdu, tbhdu])            # Creation of the new HDU object

hdulist.writeto(filename)  # output_verify='exception' )                # Writing the new HDU object on the new fits file
hdulist.close()

if args.plot : 
	fi.info(filename)

	FileFits = pf.Arch(filename)
	FileFits.Dyn_spec_structure()
	ArrayTF = FileFits.data
	ListF=np.linspace(FileFits.lofreq,FileFits.hifreq,len(ArrayTF[0]))
	ListT=np.linspace(0,FileFits.Tobs,len(ArrayTF[:,0]))

	TempsAmplobs = []
	#TempsAmplNorm =[]
	for j in range(len(ListT)):
		TempsAmplobs+=[sum(ArrayTF[j,:])/float(len(ArrayTF[j,:]))]
		#TempsAmplNorm +=[



	h=axs[1,1].pcolormesh(ListT, ListF ,ArrayTF.T)
	axs[1,1].set_xlabel('Temps(s)',fontsize = 15)
	axs[1,1].set_ylabel('Frequence(MHz)',fontsize = 15)
	#axs[0,0].colorbar()

	axs[0,1].plot(ListT,TempsAmplobs)
	axs[0,1].set_ylabel('Amplitude',fontsize = 15)
	axs[0,1].grid()
	#axs[0,0].colorbar()
	plt.show()
