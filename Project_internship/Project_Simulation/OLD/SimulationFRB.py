# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
from matplotlib.gridspec import GridSpec

ScatteringMode= False
noiseMode= False
RFIMode = False
SNRoutput = False
Polynome = True
dedispertion = False

TempsMax=1000
StandardDeviationPulse=0.001
ChanelFreq = 192
Ds=0.0209
ChanelTemp=int(TempsMax/Ds)
DM=218.9
energyPulse=float(1)
frequencyStart =float(40) 	
frequencyEnd = frequencyStart + 37.5
bw = frequencyEnd-frequencyStart
nameImage='FRB180916_E_'+ str(energyPulse) +'_D_'+ str(StandardDeviationPulse)+'.png'

def pulseModel(energyPulse, pos):
	g1 = models.Gaussian1D(energyPulse, pos, StandardDeviationPulse)
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
	ListX = np.linspace(Fs,Fe,ChanelFreq)
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


frequencyList = [frequencyStart]
ListTdm=[DM*4.15e3*(1/(frequencyList[-1]**2))]

if Polynome : AmpliBandFreq = FrenquencyBand(frequencyStart,frequencyEnd,ChanelFreq)
for i in range(0,ChanelFreq-1):
	frequencyList += [frequencyList[-1]+round((bw/(ChanelFreq-1)),1)]
	ListTdm += [DM*4.15e3*(1/(frequencyList[-1]**2))] 
	ListTdm[-1] = 450 
print(soustraire_liste(ListTdm,ListTdm[-1])) ## Remettre la FRB Simuler à zéros.
#print(len(frequencyList))
#print(ListTdm)
TimeFrequency = np.zeros((ChanelFreq,ChanelTemp))
time = np.linspace(0,TempsMax,ChanelTemp)

if ScatteringMode : timeConvolve=np.linspace(-300,300,6000)
if SNRoutput : 
	StartSignal = ListTdm[-1]-10 #Valeur arbitraire
	if ScatteringMode : ENDsignal = ListTdm[0]+310 #Scaterring + 10 s
	else: ENDsignal = ListTdm[0]+ 10
#print(StartSignal,ENDsignal)
#print(time)
#print(len(ListTdm))

for i in range(len(ListTdm)):
	if Polynome : 
		energyPulseFreq = energyPulse*AmpliBandFreq[i]
		g1 = models.Gaussian1D(energyPulseFreq, ListTdm[i], StandardDeviationPulse)
	else: 
		g1 = models.Gaussian1D(energyPulse, ListTdm[i], StandardDeviationPulse)
	signalFi = g1(time)
	
	if ScatteringMode :
		Tau=0.00105*(frequencyList[i]/600)**(-4)
		Courbscatt = np.zeros(len(timeConvolve))
		#print(Tau)
		for indice in range(len(timeConvolve)):
			if timeConvolve[indice] >= 0:
				Courbscatt[indice] = np.exp(-1*timeConvolve[indice]/Tau)
				
		Signal=(np.convolve(Courbscatt,signalFi,mode='same'))
		if max(Signal) != 0 :
			if Polynome : Signal = Signal*energyPulseFreq/max(Signal)
			else : Signal = Signal*energyPulse/max(Signal)
			
	else : 
		Signal=signalFi
		if max(Signal) != 0 :
			if Polynome : Signal = Signal*energyPulseFreq/max(Signal)
			else : Signal = Signal*energyPulse/max(Signal)
	if noiseMode : 
		noise = (np.random.randn(ChanelTemp))*2
		TimeFrequency[i] = Signal+noise
	else : 
		TimeFrequency[i] = Signal
	#print(max(signalFi))
if RFIMode:
	TimeFrequency[InterferenceFreq(),:]=10
	TimeFrequency[:,InterferenceTime()]=10 

fig,axs = plt.subplots(2,2)
PlotT, PlotF = np.meshgrid(time, frequencyList)
h = axs[0,0].contourf(PlotT, PlotF,TimeFrequency,cmap='viridis',levels=20)
#plt.axis('scaled')
#plt.colorbar()
#ax1.xticks(size = 13)
#ax1.yticks(size =13)
axs[0,0].set_title('FRB20220912A',fontsize = 18)
axs[0,0].set_xlabel('Time(s)',fontsize = 15)
axs[0,0].set_ylabel('Frequency(MHz)',fontsize = 15)
axs[0,0].legend(fontsize=10)
axs[0,0].grid()
FreqAmpl = []
for i in range(len(frequencyList)):
	FreqAmpl+=[sum(TimeFrequency[i])/len(time)]
p = np.polyfit(frequencyList,FreqAmpl,4)
#axs[0,1].set_title(p)
axs[0,1].plot(FreqAmpl,frequencyList)
axs[0,1].set_ylim(frequencyStart,frequencyEnd)
axs[0,1].set_ylabel('Frequency(MHz)',fontsize = 15)
axs[0,1].set_xlabel('Amplitude',fontsize = 15)
axs[0,1].grid()
TempsAmpl = []
MatriceTempsAmpl = np.array(TimeFrequency)
for j in range(len(time)):
	TempsAmpl+=[sum(MatriceTempsAmpl[:,j])/len(frequencyList)]
axs[1,0].plot(time,TempsAmpl)
axs[1,0].set_xlim(0, TempsMax)
axs[1,0].set_xlabel('Time(s)',fontsize = 15)
axs[1,0].set_ylabel('Amplitude',fontsize = 15)
axs[1,0].grid()

time4 = np.linspace(-1,1,int(2/0.0209))

axs[1,1].plot(time4,models.Gaussian1D(energyPulse, 0, 0.005)(time4))
#axs[1,1].set_title('Impulsion',fontsize = 18)
axs[1,1].set_xlabel('Time(s)',fontsize = 15)
axs[1,1].set_ylabel('Energy',fontsize = 15)
plt.tight_layout()
plt.show()


fig = plt.figure()
gs = GridSpec(2,3,figure=fig)
axs2 = fig.add_subplot(gs[1,:-1])
axs1 = fig.add_subplot(gs[0,:-1],sharex=axs2)
axs3 = fig.add_subplot(gs[1,-1],sharey=axs2)




axs2.contourf(PlotT, PlotF,TimeFrequency,cmap='viridis',levels=20)
axs2.set_xlabel('Time(s)',fontsize = 20)
axs2.set_xlim((0,TempsMax))
axs2.set_ylim((frequencyStart,frequencyEnd))
axs2.set_ylabel('Frequency(MHz)',fontsize = 20)
axs2.grid()
#axs[0,0].colorbar()

plt.setp(axs3.get_yticklabels(), visible=False)
#axs[0,0].colorbar()
axs3.plot(FreqAmpl,frequencyList)
axs3.set_xlabel('Amplitude',fontsize = 20)
axs3.set_ylim(frequencyStart,frequencyEnd)
axs3.grid()

plt.setp(axs1.get_xticklabels(), visible=False)
axs1.plot(time,TempsAmpl)
axs1.set_ylabel('Amplitude',fontsize = 20)
axs1.set_xlim((0,TempsMax))
axs1.grid()
plt.tight_layout()
plt.savefig(nameImage)
plt.show()

	
plt.figure()
plt.plot(time,TimeFrequency[175])
plt.figure()
plt.plot(time,TimeFrequency[90])
plt.figure()
plt.plot(time,TimeFrequency[15])
#plt.show()

if dedispertion:
	
	plt.figure()
	for i in range(len(ListTdm)):
		TimeFrequency[i]=np.roll(TimeFrequency[i],-int(ListTdm[i]/Ds))
	PlotT, PlotF = np.meshgrid(time, frequencyList)
	h = plt.contourf(PlotT, PlotF,TimeFrequency,cmap='viridis',levels=10)
	#plt.axis('scaled')
	#plt.colorbar()
	#ax1.xticks(size = 13)
	#ax1.yticks(size =13)
	plt.title('FRB20180916B',fontsize = 18)
	plt.label('Temps(s)',fontsize = 15)
	plt.ylabel('Frequence(MHz)',fontsize = 15)
	plt.legend(fontsize=10)
	plt.grid()
	plt.show()
