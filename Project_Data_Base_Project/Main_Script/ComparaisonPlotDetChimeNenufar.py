import numpy as np
from datetime import datetime, timedelta
from astropy.time import Time
import matplotlib.pyplot as plt
filePathDataNenufar = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/NenufarTF/DataBase_NenufarTF.txt'
#filePathDataChime = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/Chime/DataBase_Chime_edit.txt'
filePathDataChime='/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/Fast/DataBase_Fast.txt'
FichierNenufar = open(filePathDataNenufar,"r")
linesNenufar= FichierNenufar.readlines()
FichierNenufar.close()

FichierChime = open(filePathDataChime,"r")
linesChime= FichierChime.readlines()
FichierChime.close()
## Nenufar Traitement
nameFRB='FRB20220912A'
PeriodActivity=4
AddDay=3

def FunListActFrb(dateDetection, TimeFRBactivity_day): #dateDetection en Y-M-D
	listDate = []
	format_date = '%Y%m%d'
	date_obj = datetime.strptime(dateDetection, format_date)
	for i in range(-TimeFRBactivity_day,TimeFRBactivity_day+1):
		nouvelle_date_obj = date_obj + timedelta(days=i)
		nouvelle_date = nouvelle_date_obj.strftime(format_date)
		listDate += [nouvelle_date]
	return listDate

def FindCorrelationBtwObservationAndDetection(dateNenufar,dateChime,PeriodActivity): 
	listCorrelation = []
	for detectionDay in dateChime:
		detection = True
		for indiceObservation in range(len(dateNenufar)):
			if dateNenufar[indiceObservation] in FunListActFrb(str(detectionDay),PeriodActivity):
				if detection : 
					listCorrelation += [[detectionDay]]
					detection = False	
				listCorrelation[-1] += [[dateNenufar[indiceObservation]]]
				
	return listCorrelation

def CreationLisObs(lines,nameFRB):
	OnlyOne=True
	ListInfo=["",""]
	ListFits=[]
	ListInfoFrb=[]
	ListObsName=[]
	header = lines[0]

	Path=False
	if 'Path' in header.replace('\n','').split():
		Path=True

	#print(header)

	for Info in lines[1:]:
		goodDateBool=True
		Info=Info.replace('\n','')
		if(Info[0].isdigit()):
			#print(Info)
			date_obj = datetime.strptime(Info, "%Y%m%d")
			time_obj = Time(str(date_obj), format='iso')
			mjd = time_obj.mjd
			#print(mjd)
			#if StartD: 
			#	if float(mjd) < float(StartDate):
			#		goodDateBool=False
			#if EndD:
			#	if float(mjd) > float(EndDate):
			#		goodDateBool=False
			if goodDateBool:
				#ListInfo[1]=mjd
				ListInfo[1]=Info
				ListInfoFrb+=[ListInfo]
			ListInfo=["",""]
		elif Info[0]=='/' and Path:
			ListFits+= [Info]
		else:
			ListInfo[0]=Info
			if Info not in ListObsName:
				ListObsName+=[Info]
			
	ListObs=ListObsName
	if OnlyOne and nameFRB in ListObs: ListObs=[nameFRB]
	del ListObsName
	if len(ListObs) == 0 : 
		print("Pas de correspondance")
		exit()
	ListObs.sort()
	ListDate=[None]*len(ListObs)
	for obs in ListInfoFrb:
	#print(obs[0])
		if obs[0] in ListObs:
			index = ListObs.index(obs[0])
			if ListDate[index] == None:
				ListDate[index]=[obs[1]]
			else :
				ListDate[index]+=[obs[1]]
	return ListObs,ListDate[0]
	
	
## Modify 
#filePathDataChime='/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/Fast/DataBase_Fast.txt'




ListObsNenufar,ListDateNenufar=CreationLisObs(linesNenufar,nameFRB)
ListObsChime,ListDateCHime=CreationLisObs(linesChime,nameFRB)
print(ListObsNenufar)
print(ListDateNenufar)
print(ListObsChime)
print(ListDateCHime)
MatriceCorrelation=FindCorrelationBtwObservationAndDetection(ListDateNenufar,ListDateCHime,PeriodActivity+AddDay)
print(len(MatriceCorrelation))
IndiceStart=''
IndiceFin=''
ListIndiceX=[]
ListIndiceNonsort=[]
print(MatriceCorrelation)
for indice in range(len(MatriceCorrelation)):
	DateDetection=MatriceCorrelation[indice][0]
	date_obj = datetime.strptime(DateDetection, "%Y%m%d")
	time_obj = Time(str(date_obj), format='iso')
	mjd = time_obj.mjd
	ListIndiceX+=[mjd]
	ListIndiceNonsort+=[mjd]
	if IndiceStart=='' and IndiceFin=='':
		IndiceStart=mjd
		IndiceFin=mjd
	else:
		if mjd < IndiceStart:
			IndiceStart=mjd
		if mjd > IndiceFin:
			IndiceFin=mjd
ListIndiceX.sort()
listIndicdYMD=[]
for julian_date in ListIndiceX:
    print(julian_date)
    strjulian_date=int(julian_date)
    print(strjulian_date)
    epoch = datetime(1858, 11, 17)
    delta = timedelta(days=strjulian_date)
    date = epoch + delta
    formatted_date = date.strftime("%Y%m%d")
    listIndicdYMD+=[formatted_date]
print(listIndicdYMD)
print(IndiceStart,IndiceFin)
print(ListIndiceX)
Yplot = np.zeros((((PeriodActivity+AddDay)*2+1),len(ListIndiceX)))
for i in range(len(ListIndiceX)):
	for j in range((PeriodActivity+AddDay)*2+1):	
		Yplot[j][i]=None 
		ListeTime = FunListActFrb(str(listIndicdYMD[i]),PeriodActivity+AddDay)
		indexCorr = ListIndiceNonsort.index(ListIndiceX[i])
		for k in range(1,len(MatriceCorrelation[indexCorr])):
			indexDiff = ListeTime.index(MatriceCorrelation[indexCorr][k][0])
			Yplot[indexDiff][i] = indexDiff-PeriodActivity-AddDay
plt.figure(figsize=(20,6))	
plt.scatter(listIndicdYMD, [None]*len(listIndicdYMD), color='r', marker='x',s=180, label='Nenu_Obs_Fast')		
for i in range(len(Yplot)):
	plt.scatter(listIndicdYMD, Yplot[i], color='r', marker='x',s=180)
plt.fill_between(listIndicdYMD, -PeriodActivity,PeriodActivity , color='r', alpha=0.2)	
## End Modify
filePathDataChime = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/Chime/DataBase_Chime_edit.txt'
FichierChime = open(filePathDataChime,"r")
linesChime= FichierChime.readlines()
FichierChime.close()

ListObsNenufar,ListDateNenufar=CreationLisObs(linesNenufar,nameFRB)
ListObsChime,ListDateCHime=CreationLisObs(linesChime,nameFRB)
print(ListObsNenufar)
print(ListDateNenufar)
print(ListObsChime)
print(ListDateCHime)
MatriceCorrelation=FindCorrelationBtwObservationAndDetection(ListDateNenufar,ListDateCHime,PeriodActivity+AddDay)
print(len(MatriceCorrelation))
IndiceStart=''
IndiceFin=''
ListIndiceX=[]
ListIndiceNonsort=[]
print(MatriceCorrelation)
for indice in range(len(MatriceCorrelation)):
	DateDetection=MatriceCorrelation[indice][0]
	date_obj = datetime.strptime(DateDetection, "%Y%m%d")
	time_obj = Time(str(date_obj), format='iso')
	mjd = time_obj.mjd
	ListIndiceX+=[mjd]
	ListIndiceNonsort+=[mjd]
	if IndiceStart=='' and IndiceFin=='':
		IndiceStart=mjd
		IndiceFin=mjd
	else:
		if mjd < IndiceStart:
			IndiceStart=mjd
		if mjd > IndiceFin:
			IndiceFin=mjd
ListIndiceX.sort()
listIndicdYMD=[]
for julian_date in ListIndiceX:
    print(julian_date)
    strjulian_date=int(julian_date)
    print(strjulian_date)
    epoch = datetime(1858, 11, 17)
    delta = timedelta(days=strjulian_date)
    date = epoch + delta
    formatted_date = date.strftime("%Y%m%d")
    listIndicdYMD+=[formatted_date]
print(listIndicdYMD)
print(IndiceStart,IndiceFin)
print(ListIndiceX)
Yplot = np.zeros((((PeriodActivity+AddDay)*2+1),len(ListIndiceX)))
for i in range(len(ListIndiceX)):
	for j in range((PeriodActivity+AddDay)*2+1):	
		Yplot[j][i]=None 
		ListeTime = FunListActFrb(str(listIndicdYMD[i]),PeriodActivity+AddDay)
		indexCorr = ListIndiceNonsort.index(ListIndiceX[i])
		for k in range(1,len(MatriceCorrelation[indexCorr])):
			indexDiff = ListeTime.index(MatriceCorrelation[indexCorr][k][0])
			Yplot[indexDiff][i] = indexDiff-PeriodActivity-AddDay
#plt.figure(figsize=(20,4))	
plt.scatter(listIndicdYMD, [None]*len(listIndicdYMD), color='b', marker='o',s=180, label='Nenu_Obs_Chime')		
for i in range(len(Yplot)):
	plt.scatter(listIndicdYMD, Yplot[i], color='b', marker='o',s=180)
	

	
	
plt.xticks(rotation=45,size = 14)
plt.yticks(size =13)

plt.fill_between(listIndicdYMD, -PeriodActivity,PeriodActivity , color='r', alpha=0.2, label='activity window :'+str((PeriodActivity))+' days')
#plt.fill_between(listIndicdYMD, -PeriodActivity+3.6 ,PeriodActivity+3.6 , color='g', alpha=0.1, label='delay window :'+str(3.6)+' days')
	#for i, highlight in enumerate(highlight_x):
	#	if highlight == 1:
	#		plt.text(i, plotX[i], fontweight='bold')
plt.title('Nenufar Observation Date in function of Chime and Fast Detection Date on FRB20220912A',fontsize = 18)
plt.xlabel('Detection Date From FAST or CHIME(YMD)',fontsize = 16)
plt.ylabel('Obs and Detection Delay(Day)',fontsize = 16)
plt.tight_layout()
plt.legend(fontsize=16,loc='upper left')
plt.grid()
plt.show()	
