# coding=utf-8
import json
import sys
from datetime import datetime, timedelta
import subprocess
import functionObservation
import matplotlib.pyplot as plt
import numpy as np

filenamejson='./ChimeData.json'

mode=""
ListArg=[]

for arg in sys.argv: 
	ListArg+=[arg]
	print(arg)
lArg=ListArg[1:]
## TO DO sécurité sur les arguments
NomFrbChime=lArg[0]
MethodPlot =lArg[1]
DataBase = lArg[2]
PeriodActivity = int(lArg[3])
AddDay = int(lArg[4])
DelayWindow = int(lArg[5])

 ## Si float remplacer int par float plus bas
NomFrbNenufar=functionObservation.Name_Frb_Chime_To_Frb_Nenufar(NomFrbChime)
dateChimeDetection = functionObservation.FrbToDetectionChime(NomFrbChime,filenamejson)

if DataBase == "PULSAR" : dateNenufarObservation,timeNenufarObservation,durationNenufarObservation = functionObservation.FrbToObservation_Duration(NomFrbNenufar)
if DataBase == "TF" : dateNenufarObservation,timeNenufarObservation,durationNenufarObservation = functionObservation.FrbToObservation_Duration_tf(NomFrbNenufar)
#ArrayCorrelation = functionObservation.FindCorrelationBtwObservationAndDetection(dateNenufarObservation,timeNenufarObservation,durationNenufarObservation,dateChimeDetection,PeriodActivity+AddDay)



#To Do verifier que ArrayCorrelation n'est pas vide

# A travailler !! 
# Initialisation des listes pour les données à afficher
#x = [] # Heures des observations
#y = [] # Jours de détection
#sizes = [] # Durées des observations

plt.close()


if MethodPlot == 'Test': ## En experimentation
	print(sorted(dateNenufarObservation),'\nNomFrbNenufar : ',NomFrbNenufar,'First Detection: ',sorted(dateNenufarObservation)[0],'Last Detection: ',sorted(dateNenufarObservation)[-1],'numbre of burst find: :',len(dateNenufarObservation))
		


if MethodPlot == '1': ## En experimentation 

	print(ArrayCorrelation)
	# Liste des couleurs à utiliser pour les jours de détection
	xPlot=functionObservation.FunListActFrb(ArrayCorrelation[0][0].split()[0],PeriodActivity+AddDay)
	print("Xplot: ",xPlot,"\nTailleXPlot: ",len(xPlot))
	Yplot= np.zeros(((len(ArrayCorrelation[0])-1),len(xPlot)))
	print('ArrayCorrelation[0]: ',ArrayCorrelation[0])
	for i in range(1,len(ArrayCorrelation[0])):
		for j in range(len(xPlot)):
			#print(ArrayCorrelation[0][i][0],xPlot[j])	
			if ArrayCorrelation[0][i][0] == xPlot[j]:
				Yplot[i-1][j]=int(i)
			else : Yplot[i-1][j]= None
	
	print('Yplot: ', Yplot)
	for i in range(len(Yplot)):
		plt.scatter(xPlot, Yplot[i], label='NenufarObservation'+ArrayCorrelation[0][i+1][0])	
	plt.xlim(xPlot[0], xPlot[-1])

	# Ajouter un titre et des étiquettes d'axe
	plt.title('ObservationNenufarOn'+NomFrbChime+'for a dectction at'+ArrayCorrelation[0][0])
	plt.xlabel('Date')
	plt.ylabel('ObservationNumber')
	# Ajouter une légende
	plt.legend()

	# Afficher le graphique
	plt.show()	

if MethodPlot == 'INFO' or MethodPlot =='ALL_DATA':	 
	
	plotX=[]
	
	for i in dateChimeDetection:
		plotX += [i.split()[0]]
	listCorrelation=[]
	for i in range(len(ArrayCorrelation)):
		listCorrelation += [ArrayCorrelation[i][0].split()[0]] 


	if MethodPlot == "INFO":
		indexDebut = plotX.index(listCorrelation[0])
		indexFin =  plotX.index(listCorrelation[-1])
		plotX = plotX[indexDebut:indexFin+1]


	Yplot = np.zeros((((PeriodActivity+AddDay)*2+1),len(plotX)))
	for i in range(len(plotX)):
		for j in range((PeriodActivity+AddDay)*2+1):	
				Yplot[j][i]=None
		if plotX[i] in listCorrelation : 
			ListeTime = functionObservation.FunListActFrb(plotX[i],PeriodActivity+AddDay)
			for j in range((PeriodActivity+AddDay)*2+1):	
				indexCorr = listCorrelation.index(plotX[i])
				for k in range(1,len(ArrayCorrelation[indexCorr])):
					indexDiff = ListeTime.index(ArrayCorrelation[indexCorr][k][0])
					Yplot[indexDiff][i] = indexDiff-PeriodActivity-AddDay
		
		
	#for i in range(len(plotX)) :
	#	plotX[i] = plotX[i][2:]
	#	plotX[i] = plotX[i].replace("-","")


	#for i in range(len(plotX)):
	#	highlight_x=[]
	#	for j in range[
	#	if Yplot[i] == [None]*((PeriodActivity+AddDay)*2+1):
	#		highlight_x+=[0]
	#	else : 
	#		highlight_x+=[1]

	for i in range(len(Yplot)):
		if DataBase == "TF":
			plt.scatter(plotX, Yplot[i], color='r', marker='x')
		if DataBase == "PULSAR":
			plt.scatter(plotX, Yplot[i], color='b', marker='o')	
	plt.xticks(rotation=45)
	plt.fill_between(plotX, -PeriodActivity,PeriodActivity , color='r', alpha=0.2, label='activity window :'+str((PeriodActivity))+' days')
	plt.fill_between(plotX, PeriodActivity ,PeriodActivity+DelayWindow , color='g', alpha=0.2, label='delay window :'+str(DelayWindow)+' days' )
	#for i, highlight in enumerate(highlight_x):
	#	if highlight == 1:
	#		plt.text(i, plotX[i], fontweight='bold')
	plt.title('Correlation Btw Chime Detection And Nenufar Observation On '+NomFrbChime,)
	plt.xlabel('Detection Date From CHIME(YMD)')
	plt.ylabel('Delay Beteween Observation and Detection(Day)')
	plt.grid()
	plt.legend()
	plt.show()	




	




