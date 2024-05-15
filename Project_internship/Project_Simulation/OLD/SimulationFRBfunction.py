#Import
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting

## Mode
ScatteringMode=True
noiseMode= False
RFIMode = False
SNRoutput = False
Polynome = True
dedispertion = False


##Parametre
ChanelFreq = 192
Ds=0.02
ChanelTemp=int(1500/Ds)
DM=348.8
energyPulse=40
frequencyStart = 40 	
frequencyEnd = 80


##Fun
def pulseModel(energyPulse, pos):
	g1 = models.Gaussian1D(energyPulse, pos, 1)
	return g1
	
def noiseModel(energyNoise):
	samples = np.random.randn(ChanelTemp)
def InterferenceFreq():
	f = np.random.randint(ChanelFreq)
	return f
def InterferenceTime():
	t = np.random.randint(ChanelTemp)
	return t

def FrenquencyBand(Fs,Fe,Fc):
	ListX = np.linspace(Fs,Fe,192)
	alpha = -1
	beta = Fs+Fe
	gama = -(alpha*Fs*Fs + beta*Fs)
	Y = alpha*ListX*ListX + beta*ListX + gama
	Y =Y/max(Y)
	return Y
	
def soustraire_liste(liste, nombre):
    resultat = []
    for element in liste:
        resultat.append(element - nombre)
    return resultat

def SimulationFRB(time,energy)
	frequencyList = [frequencyStart]
	ListTdm=[DM*4.15e3*(1/(frequencyList[-1]**2))]
	if Polynome : AmpliBandFreq = FrenquencyBand(frequencyStart,frequencyEnd,ChanelFreq)
	for i in range(0,ChanelFreq-1):
		frequencyList += [frequencyList[-1]+round((40/(ChanelFreq-1)),1)]
		ListTdm += [DM*4.15e3*(1/(frequencyList[-1]**2))] 
	ListTdm=soustraire_liste(ListTdm,ListTdm[-1])
	ListTdm=add_list(ListTdm,float(TimeFRB))
	TimeFrequency = np.zeros((ChanelFreq,ChanelTemp))
	time = np.linspace(0,1500,ChanelTemp)

	if ScatteringMode : timeConvolve=np.linspace(-300,300,6000)
	if SNRoutput : 
		StartSignal = ListTdm[-1]-10 #Valeur arbitraire
		if ScatteringMode : ENDsignal = ListTdm[0]+310 #Scaterring + 10 s
		else: ENDsignal = ListTdm[0]+ 10
	for i in range(len(ListTdm)):
		if Polynome : 
			energyPulseFreq = energyPulse*AmpliBandFreq[i]
			g1 = models.Gaussian1D(energyPulseFreq, ListTdm[i], 1)
		else: 
			g1 = models.Gaussian1D(energyPulse, ListTdm[i], 1)
		signalFi = g1(time)
		if ScatteringMode :
			Tau=0.00105*(frequencyList[i]/600)**(-4)
			Courbscatt = np.zeros(len(timeConvolve))
			print(Tau)
			for indice in range(len(timeConvolve)):
				if timeConvolve[indice] >= 0:
					Courbscatt[indice] = np.exp(-1*timeConvolve[indice]/Tau)
					
			Signal=(np.convolve(Courbscatt,signalFi,mode='same'))
			if max(Signal) != 0 :
				if Polynome : Signal = Signal*energyPulseFreq/max(Signal)
				else : Signal = Signal*energyPulse/max(Signal)
		else : 
			Signal=signalFi
		if noiseMode : 
			noise = (np.random.randn(ChanelTemp))*2
			TimeFrequency[i] = Signal+noise
		else : 
			TimeFrequency[i] = Signal
		#print(max(signalFi))
	if RFIMode:
		TimeFrequency[InterferenceFreq(),:]=10
		TimeFrequency[:,InterferenceTime()]=10 
return TimeFrequency
