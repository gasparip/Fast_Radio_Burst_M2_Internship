
FpythonPulsarDiff = "/data/pgaspari/WeeklyReport/.processFile/FpythonPulsarDiff.txt"
FpythonTfDiff = "/data/pgaspari/WeeklyReport/.processFile/FpythonTfDiff.txt"
FmetaDataNenufar = "/data/pgaspari/WeeklyReport/.processFile/metaDataPythonFile.txt"
ToDoFile="/data/pgaspari/WeeklyReport/.processFile/ToDoFile.txt"
ForPythonToShToPDF="/data/pgaspari/WeeklyReport/.processFile/ForPythonToShToPDF.txt"

ListTf=[]
ListPulsar=[]
ListInfo=["",""]
ListFits=[]
ListMetaData = [['FRBName'],['DM']]
modeProcess =True
InputParametrValue = [[3,3,0.5,0.5],[3,2.5,0.5,0.5],[3.5,3.5,0.5,0.5]]

FichierPulsar = open(FpythonPulsarDiff,"r")
linesPulsar= FichierPulsar.readlines()
FichierPulsar.close()

FichierTF = open(FpythonTfDiff,"r")
linesTF = FichierTF.readlines()
FichierTF.close()

FichierMetaData = open(FmetaDataNenufar,"r")
linesMeta = FichierMetaData.readlines()
FichierMetaData.close()


for MetaData in linesMeta[1:]:
	MetaData=MetaData.replace('\n','')
	if str(MetaData).isdigit():
		ListMetaData[1]+=[MetaData]
	else : 
		ListMetaData[0]+=[MetaData]

for InfoPulsar in linesPulsar:
	InfoPulsar=InfoPulsar.replace('\n','')
	if(InfoPulsar[0].isdigit()):
		ListInfo[1]=InfoPulsar
		ListPulsar+=[ListInfo]
		ListInfo=["",""]
	elif InfoPulsar[0]=='/':
		ListFits+= [InfoPulsar]
	else:
		ListInfo[0]=InfoPulsar

print(ListPulsar)
ListInfo=["",""]
		
for InfoTf in linesTF:
	InfoTf=InfoTf.replace('\n','')
	if(InfoTf[0].isdigit()):
		ListInfo[1]=InfoTf
		ListTf+=[ListInfo]
		ListInfo=["",""]
	else:
		ListInfo[0]=InfoTf

print(ListTf)

fichierReturnText = open(ForPythonToShToPDF, "w")
Ligne="\n"
fichierReturnText.write(Ligne)
for Obs in ListTf:
	if Obs in ListPulsar:
		indice = ListPulsar.index(Obs)
		print("L\'Observation de "+str(Obs[0])+" le "+str(Obs[1])+" est présent dans le mode PULSAR")
		print("PATH OBSERVATION "+ ListFits[indice])
		if Obs[0] in ListMetaData[0]:
			print("L\'Observation de "+str(Obs[0])+" est dans la base de donnée et le DM est de "+str(ListMetaData[1][ListMetaData[0].index(Obs[0])]))
			Ligne="L\'Observation de "+str(Obs[0])+" observé en TF mode le "+str(Obs[1])+" est présent dans le mode PULSAR et dans la base de donnée \n"
			Ligne+="Le DM est de "+str(ListMetaData[1][ListMetaData[0].index(Obs[0])])+" pc/cm3 et le path est "+ListFits[indice]+"\n\n"
		else :
			print("!!!!!!! Warning, pas dans la base de donnée")
			Ligne="L\'Observation de "+str(Obs[0])+" observé en TF mode le "+str(Obs[1])+" est présent dans le mode PULSAR mais pas dans la base de donnée \n"
			Ligne+="!!!!! Le traitement n'est pas possible, Path : "+ListFits[indice]+"\n\n"
	else: 
		print("WARNING !!!!!!!! L\'Observation de "+str(Obs[0])+" le "+str(Obs[1])+" n' est pas présente dans le mode PULSAR")
		Ligne="!!!!!!!! WARNING !!!!!!!! L\'Observation de "+str(Obs[0])+" le "+str(Obs[1])+" n'est pas présente dans le mode PULSAR \n\n"
	fichierReturnText.write(Ligne)
	print()
fichierReturnText.close()	

if modeProcess : 
	fichierToDo = open(ToDoFile, "w")
	Ligne=""
	for ObsPulsar in ListPulsar:
		if ObsPulsar[0] in ListMetaData[0]:
			DMhigh= int(ListMetaData[1][ListMetaData[0].index(ObsPulsar[0])]) + 20 
			DMlow= int(ListMetaData[1][ListMetaData[0].index(ObsPulsar[0])]) - 20 
			for i in range(len(InputParametrValue)):
				SigmaF=InputParametrValue[i][0]
				SigmaT=InputParametrValue[i][1]
				BerrF=InputParametrValue[i][2]
				BerrT=InputParametrValue[i][3]
				listPar = [DMhigh,DMlow,SigmaF,SigmaT,BerrF,BerrT]
				Ligne+= str(ObsPulsar[0])+" "+str(ObsPulsar[1])+" "+str(ListMetaData[1][ListMetaData[0].index(ObsPulsar[0])])+" "+ ListFits[ListPulsar.index(ObsPulsar)]
				for j in range(len(listPar)):
					Ligne+=" "+str(listPar[j])
				Ligne+="\n"
				fichierToDo.write(Ligne)
				Ligne=""
	# Écrire des lignes dans le fichier
		else : 
			Ligne=""
	fichierToDo.close()

# Fermer le fichier


	
