import os
import numpy as np
import matplotlib.pyplot as plt


## Parametre
PathFileFits ='B0329+54_D20230311T1601_60014_252892_0063_BEAM1_0001.fits'
Pas = 0.01
STend= 4
SFend = 4
STstart= 1
SFstart= 0
STfix = 3
SFfix = 3
BerrTstart = 0.2
BerrTend = 0.6
BerrFstart = 0.25
BerrFend =1
List = [2349.8,184.5,2676.4,603.3,172.4,2155.3,1140.6,1623.0,2683.5,169.6,1617.9,586.1,2356.8,218.1,1793.8,1675.2,825.6,403.9,203.1,1690.9]
 
DM = 26.7
DMs_max = 50
DMs_min = 5
ListeDM=[round(DM-0.1,1),DM,round(DM+0.1,1)]
ModeResearch = "SPSB" 
NameDirectoryEtude= "Test_16_1_090523_ST_3_SF_3_BerrT_0.2_0.6_0.01_BerrF_0.25_1_0.01"

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
ListBerrT = np.arange(float(BerrTstart),float(BerrTend)+float(Pas), Pas)
ListBerrF = np.arange(float(BerrFstart),float(BerrFend)+float(Pas), Pas)
#ListST=[3]
#ListSF=[3]
print(ListBerrT,ListBerrF)

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

	for BerrT in ListBerrT:
		for BerrF in ListBerrF: 
			freqsig = SFfix
			timesig = STfix
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
