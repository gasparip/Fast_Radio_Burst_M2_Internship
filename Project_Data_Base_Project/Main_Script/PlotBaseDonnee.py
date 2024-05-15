# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from astropy.time import Time

#filePathData = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/NenufarPULSAR/DataBase_NenufarPULSAR.txt'
#filePathData = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/NenufarTF/DataBase_NenufarTF.txt'
filePathData = '/data/pgaspari/BaseDonneeProject/NewVersion/dataBase/Chime/DataBase_Chime.txt'
StartDate="20220601"
EndDate="2023-06-10"
StartD=False
EndD=False
ListMODE=["FRB","SGR","OTHEROBS"]
OneName=True
TelescopeName='Nenufar'
OnlyOne=False
nameFRB="FRB20220912A"
MJD=True

def IsMJD(date):
	if '-' in date:
		date=date.replace('-','')
		date_obj = datetime.strptime(date, "%Y%m%d")
		time_obj = Time(str(date_obj), format='iso')
		mjd = time_obj.mjd
		return mjd
	elif len(date) == 8:
		date=date.replace('-','')
		date_obj = datetime.strptime(date, "%Y%m%d")
		time_obj = Time(str(date_obj), format='iso')
		mjd = time_obj.mjd
		return mjd	
	elif len(date) == 5:
		return date
	else:
		return -1

#print(IsMJD(StartDate))
if StartD:
	StartDate=IsMJD(StartDate)
if EndD:
	EndDate=IsMJD(EndDate)

ListInfo=["",""]
ListFits=[]
ListInfoFrb=[]
ListObsName=[]

Fichier = open(filePathData,"r")
lines= Fichier.readlines()
Fichier.close()
header = lines[0]

Path=False
if 'Path' in header.replace('\n','').split():
	Path=True

#print(header)

for Info in lines[1:]:
	goodDateBool=True
	Info=Info.replace('\n','')
	if(Info[0].isdigit()):
		date_obj = datetime.strptime(Info, "%Y%m%d")
		time_obj = Time(str(date_obj), format='iso')
		mjd = time_obj.mjd
		if StartD: 
			if float(mjd) < float(StartDate):
				goodDateBool=False
		if EndD:
			if float(mjd) > float(EndDate):
				goodDateBool=False
		if goodDateBool:
			ListInfo[1]=mjd
			ListInfoFrb+=[ListInfo]
		ListInfo=["",""]
	elif Info[0]=='/' and Path:
		ListFits+= [Info]
	else:
		ListInfo[0]=Info
		if Info not in ListObsName:
			ListObsName+=[Info]

#print(ListInfoFrb)
#print(ListFits)
#print(ListObsName)

cntPULSAR = 0
ListPULSAR=[]
cntFRB = 0
ListFRB=[]
cntSGR = 0
ListSGR=[]
cntOtherObs = 0 
ListOther=[]

for name in ListObsName:
	if name[0] == 'B' or name[0] == 'J' :
		cntPULSAR+=1
		ListPULSAR+=[name]
	elif name[0:3] == 'FRB' :
		cntFRB+=1
		ListFRB+=[name]
	elif name[0:3] == 'SGR' :
		cntSGR+=1
		ListSGR+=[name]
	else: 
		cntOtherObs += 1
		ListOther+=[name]
#print(cntPULSAR,cntFRB,ListFRB,cntSGR,cntOtherObs)

ListObs=[]
if "PULSAR" in ListMODE: ListObs += ListPULSAR
if "FRB" in ListMODE: ListObs += ListFRB
if "SGR" in ListMODE: ListObs += ListSGR
if "OTHEROBS" in ListMODE: ListObs += ListOther
if ListMODE==[] : ListObs=ListObsName
if OnlyOne : ListObs=[nameFRB]
if OneName:
	newListObs=[]
	for i in range(len(ListObs)):
		BoolAdd=True
		nameObs=ListObs[i]
		if len(nameObs)<=10 and nameObs[0:3]=='FRB':
        		for j in range(len(ListObs)):
           			 if i != j and nameObs[3:10] in ListObs[j]:
           		         	BoolAdd = False
           		         	for obs in ListInfoFrb:
           		         		if obs[0] == nameObs: obs[0]=ListObs[j]
	if BoolAdd: newListObs+=[nameObs]

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
#print(ListObs,ListDate)

fig = plt.figure()
newyvalue = []
newsticksvalue =[]
cnt=0
for i in range(len(ListObs)):
	if ListDate[i] != None:
		yaxs = (i-cnt) *np.ones(len(ListDate[i]))
		xaxs = ListDate[i]
		plt.scatter(xaxs,yaxs,marker='x')
		newyvalue += [i-cnt]
		newsticksvalue += [ListObs[i]]
		plt.yticks(newyvalue, newsticksvalue)
	else :
		cnt+=1
		
plt.title('Chronology of observations on '+str(TelescopeName),fontsize=18)
plt.xlabel("MJD", fontsize=14)
plt.ylabel("Target Name", fontsize=14)
plt.locator_params(axis='x',nbins=20)
plt.grid()
plt.show()
	
	
