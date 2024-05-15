# coding=utf-8
import os
import numpy as np
import matplotlib.pyplot as plt


## Parametre
PathDirectory='/data/pgaspari/ParametreOptimisation/Dir_Simu_Fits/'
NameFileFits ='13sommes_1.fits'
PathFileFits = PathDirectory+NameFileFits
Pas = 0.5
STend= 3
SFend = 3
STstart=2
SFstart=2
STfix = 2.5
SFfix = 3.5
BerrT = 0.5
BerrF = 0.5
List = [' 1000\.',' 2000\.',' 3000\.' ,' 4000\.',' 5000\.',' 6000\.',' 7000\.',' 8000\.',' 9000\.',' 10000\.',' 11000\.',' 12000\.',' 13000\.']
DM = 218.9
DMs_max = 240
DMs_min = 200
ListeDM=[round(DM-1,0),DM,round(DM+1,0)]
ModeResearch = "SPSB" 
NameDirectoryEtude= "Test_16_1_100723_ST_2_3_0.5_SF_2_3_0.5_BerrT_0.5_BerrF_0.5"

strDM ="{"
for dm in ListeDM:
	strDM+=str(dm)
	if dm == ListeDM[-1]:
		break
	else : strDM+=','
strDM+="}"

print('\n	----------- COMMAND POST TREATEMENT -----------	\n')


#cmd_sys3 = "../Delete.sh"
#print(cmd_sys3)
#os.system('GREPDB="'+cmd_sys3+'"; /bin/bash -c "$GREPDB"')
#print('		./Parametre/'+ModeResearch+'/*')
#os.system('rm ./Parametre/'+ModeResearch+'/*')



print('\n	----------- COMMAND TREATEMENT -----------	\n')

#Pas = 0.1
#STend= 5
#SFend = 5
#STstart= 4
#SFstart= 4
ListST = np.arange(float(STstart),float(STend)+float(Pas), Pas)
ListSF = np.arange(float(SFstart),float(SFend)+float(Pas), Pas)
#ListST=[3]
#ListSF=[3]
print(ListST,ListSF)

### Travail uniquement sur LISTST

#Utilisation de SFfixe
#freqsig = SFfix
#timesig = STfix
#chanfrac = BerrF
#intfrac = BerrT

def caluclValueOS(strDM,fileName):
	
	print('\n	----------- COMMAND CALCUL -----------	\n')
	cmd_nbr_detection = 'cat *.singlepulse | wc -l'
	cmd_nbr_detection_sys = cmd_nbr_detection+'>>'+fileName
	cmd_nbr_bonne_detection = 'cat *DM'+strDM+'*.singlepulse | wc -l'
	cmd_nbr_bonne_detection_sys = cmd_nbr_bonne_detection+'>>'+fileName
	cmd_somme_bonne_detection_snr = 'cat *DM'+strDM+'*.singlepulse | awk \'{total += \$2} END {print total}\''
	cmd_somme_bonne_detection_snr_sys = cmd_somme_bonne_detection_snr+' >> '+fileName
	cmd_somme_total_snr= "cat *singlepulse | awk '{total += $2} END {print total}'"
	cmd_somme_total_snr_sys = cmd_somme_total_snr+'>>'+fileName
	os.system('echo cmd_nbr_detection >>'+fileName)
	os.system(cmd_nbr_detection_sys)
	print(cmd_nbr_detection_sys)
	os.system('echo cmd_nbr_bonne_detection >>'+fileName)
	os.system('GREPDB="'+cmd_nbr_bonne_detection_sys+'"; /bin/bash -c "$GREPDB"')
	print(cmd_nbr_bonne_detection_sys)
	os.system('echo cmd_somme_bonne_detection_snr >>'+fileName)
	os.system('GREPDB="'+cmd_somme_bonne_detection_snr_sys+'"; /bin/bash -c "$GREPDB"')
	print(cmd_somme_bonne_detection_snr_sys)
	os.system('echo cmd_somme_total_snr >>'+fileName)
	os.system(cmd_somme_total_snr_sys)
	print(cmd_somme_total_snr_sys)
	return 0 

mode = 'ALL'  #ALL , load, OnlySF, OnlyST
#mode2 = 'plot' #plot
#modePlot = '2D_Color' #3D ou 3D_ONE 2D_Color 3D_Special
if mode == 'TEST':
	caluclValueOS(strDM,'./text.txt')
if mode == 'ALL': #Work 
	cmd_sys3 = "../../Delete.sh"
	print(cmd_sys3)
	os.system('GREPDB="'+cmd_sys3+'"; /bin/bash -c "$GREPDB"')
	print('		../Parametre/'+ModeResearch+'/'+NameDirectoryEtude+'/*')
	os.system('rm ../Parametre/'+ModeResearch+'/'+NameDirectoryEtude+'/*')

	for ST in ListST:
		for SF in ListSF: 
			freqsig = SF
			timesig = ST
			chanfrac = BerrF
			intfrac = BerrT
			os.system('echo >NewFile.sh')
			print('echo >NewFile.sh')
			os.system('chmod 777 NewFile.sh')
			print('	chmod 777 NewFile.sh')

			cmd_sys_SPM ='csh -f `./FRB-search_PULSARmode_v2.csh '+PathFileFits+' '+str(DMs_max)+' '+str(DMs_min)+' '+str(freqsig)+' '+str(timesig)+' '+str(chanfrac)+' '+str(intfrac)+'`'
			print(cmd_sys_SPM)
			os.system('GREPDB="'+cmd_sys_SPM+'"; /bin/bash -c "$GREPDB"') ## Necessary to apply a bash script
			fileName = 'File_With_DMmax_'+str(DMs_max)+'_DMmin_'+str(DMs_min)+'_SigmaF_'+str(freqsig)+'_SigmaT_'+str(timesig)+'_BerrF_'+str(chanfrac)+'_BerrT_'+str(intfrac)
			print('fileName: ',fileName)
			for i in List:
				cmd="cat *"+strDM+"*.singlepulse | sort -k 2 -g | grep -E '"+str(i)+"' | tail -1 >>../Parametre/"+ModeResearch+"/"+NameDirectoryEtude+"/"+fileName+".txt"
				cmd_sys = 'echo "'+cmd+'">>NewFile.sh'
				print(cmd_sys)
				os.system(cmd_sys)
			os.system("echo Parametre_File_With DMmax "+str(DMs_max)+" DMmin "+str(DMs_min)+" SigmaF "+str(freqsig)+" SigmaT "+str(timesig)+" BerrF "+str(chanfrac)+" BerrT  "+str(intfrac)+" >../Parametre/"+ModeResearch+"/"+NameDirectoryEtude+"/"+fileName+".txt")
			caluclValueOS(strDM,"../Parametre/"+ModeResearch+"/"+NameDirectoryEtude+"/"+fileName+".txt")

			cmd_sys2 = "./NewFile.sh"
			print(cmd_sys2)
			os.system('GREPDB="'+cmd_sys2+'"; /bin/bash -c "$GREPDB"') ## Necessary to apply a bash script
			cmd_sys4 = "mv *singlepulse.ps ../Parametre/SinglePulseFile/"+NameDirectoryEtude+"/"+fileName+"_singlepulse.ps"
			print(cmd_sys4)
			os.system('GREPDB="'+cmd_sys4+'"; /bin/bash -c "$GREPDB"')
			cmd_sys3 = "../../Delete.sh"
			print(cmd_sys3)
			os.system('GREPDB="'+cmd_sys3+'"; /bin/bash -c "$GREPDB"')
