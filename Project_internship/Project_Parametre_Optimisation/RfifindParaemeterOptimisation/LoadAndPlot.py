from mpl_toolkits import mplot3d
import os
import numpy as np
import matplotlib.pyplot as plt

List = [2349.8,184.5,2676.4,603.3,172.4,2155.3,1140.6,1623.0,2683.5,169.6,1617.9,586.1,2356.8,218.1,1793.8,1675.2,825.6,403.9,203.1,1690.9]
mode ='load'
ModeResearch = 'SPSB'
NameTest ='Test_240423_ST_1.5_3.5_0.01_SF_0_1.5_0.01_Berr_0.35_Berrf_0.45'
## Test ligne  : ls ./Parametre/SPSB/Test_200423_ST_1_4_0.1_SF_0_4_0.1_BerrtT_0.5_Berrf_0.5/File*.txt > ./Parametre/listFileText/file_Test_200423_ST_1_4_0.1_SF_0_4_0.1_BerrtT_0.5_Berrf_0.5.txt
if mode == 'load': 
	ListTotal = [['DMmax']+['DMmin']+['SigmaF']+['SigmaT']+['BerrF']+['BerrT']+['cmd_nbr_detection']+['cmd_nbr_bonne_detection']+['cmd_somme_bonne_detection_snr']+['cmd_somme_total_snr']+List]
	lnListTotal = len(ListTotal[0])
	cmd_load_sys = "ls ./Parametre/"+ModeResearch+"/"+NameTest+"/File*.txt > ./Parametre/listFileText/file_"+NameTest+".txt"
	os.system('GREPDB="'+cmd_load_sys+'"; /bin/bash -c "$GREPDB"')
#fichier = open("./Parametre/"+ModeResearch+"/LoadModeFile.txt","r")
	fichier = open("./Parametre/listFileText/file_"+NameTest+".txt","r") ## ForTheTest
	lines = fichier.readlines()
	fichier.close()
	for k in range(len(lines)):
		ListTotal +=[[None]*lnListTotal]
	#print(ListTotal)
	#print(ListTotal[0])
	compteurFile=1
	for line in lines:
		line=line.replace('\n','')
		print(line)
		#print(line)
		#data = open("./Parametre/"+ModeResearch+"/"+line,"r")
		print("./Parametre/"+ModeResearch+"/"+NameTest+"/"+line)
		data = open(line,"r") 
		dataLines = data.readlines()
		data.close()
		#ListeTemp = [None]*lnListTotal
		compteur = 0
		for cnt in range(len(dataLines)):
			dataLine=dataLines[cnt].replace('\n','')
			#print(cnt,'\n',dataLine)
			if cnt == 0:
				information=dataLine.split()
				for cnt2 in range(len(information)):
					if information[cnt2].replace(':','') in ListTotal[0]:  ## For test enlever le remplace()
						Index = ListTotal[0].index(information[cnt2].replace(':',''))  ## For test enlever le remplace()	
						ListTotal[compteurFile][Index] = information[cnt2+1]


			elif cnt in range(1,9,2):
				dataLine=dataLine.split()[0]#A changer si normal, pour test ## For the test A enle
				if dataLine in ListTotal[0]:
					Index = ListTotal[0].index(dataLine)
					value = dataLines[cnt+1].replace('\n','')
					if value not in['',' ']:
						ListTotal[compteurFile][Index]=value
			

			elif cnt >=9:
				information=dataLine.split()
				for k in ListTotal[0]:
					if str(k) in information[2]:
						Index = ListTotal[0].index(k)				
						ListTotal[compteurFile][Index]=information[1]						
			#print(ListTotal[compteurFile])
		compteurFile+=1
	#print(ListTotal)
	ListPlot=np.array(ListTotal)
	print(ListTotal[0],ListTotal)
	

#print("0",ListPlot[1:,3])
modeCalcul = ''
SinglePulseSearch = False
rapport= True
mode2 = 'plot'
#modePlot='3D_observation'
modePlot = '2D_Color_ST_SF'
if mode2 == 'plot':
	
		
	#plt.scatter(plotX, [None]*len(plotX), color='r', marker='x',s=180, label='TF_MODE')
		
	#plt.scatter(plotX,[None]*len(plotX), color='b', marker='o',s=120, alpha = 0.7,  label='PULSAR_MODE')
	#for i in range(len(Yplot)):
	#	if dataB == "TF":
	#		plt.scatter(plotX, Yplot[i], color='r', marker='x',s=180)

	#	if dataB == "PULSAR":
	#		plt.scatter(plotX, Yplot[i], color='b', marker='o', alpha=0.6,s=120 )
	

	#if lArg[2] == "PULSAR_TF" :	
	#	if len(plotXtot[0])>len(plotXtot[1]):plotX=plotXtot[0]
	#	else : plotX=plotXtot[1]
	#plt.fill_between(plotX, -PeriodActivity,PeriodActivity , color='r', alpha=0.2, label='activity window :'+str((PeriodActivity))+' days')
	#plt.fill_between(plotX, -PeriodActivity+3.6 ,PeriodActivity+3.6 , color='g', alpha=0.1, label='delay window :'+str(3.6)+' days')
	tuplePlot=()
	Pas = 0.5
	STend= 10
	SFend = 10
	STstart= 0.5
	SFstart= 0.5
	PlotX=[]
	PlotY=[]
	ListST = np.arange(float(STstart),float(STend)+float(Pas), Pas)
	ListSF = np.arange(float(SFstart),float(SFend)+float(Pas), Pas)
	#value=float(2349.8)
	List.sort()
	if modePlot=='2D_ALL':
		plt.figure()
		#for value in List:
		#	PlotX=[]
		#	PlotY=[]
		#	for line in range(1,len(ListPlot[:,0])):
		#		if float(ListPlot[line,ListTotal[0].index('SigmaT')]) == 2.0:
		#			y= ListTotal[line][ListTotal[0].index(value)]
		#			if y is None:PlotY+=[y]
		#			else : PlotY+=[float(y)]
		#			PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaF')])]
		#	plt.scatter(PlotX, PlotY, marker='o', alpha=0.6,s=120,label=str(value))
		
		for value in List:
			PlotX=[]
			PlotY=[]
			for line in range(1,len(ListPlot[:,0])):
				if float(ListPlot[line,ListTotal[0].index('SigmaT')]) == 8.0:
					y= ListTotal[line][ListTotal[0].index(value)]
					if y is None:PlotY+=[y]
					else : PlotY+=[float(y)]
					PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaF')])]
			plt.scatter(PlotX, PlotY, marker='o', alpha=0.6,s=120,label=str(value))
	
	#for line in range(1,len(ListPlot[:,0])):
		#if float(ListPlot[line,ListTotal[0].index('SigmaF')]) == 2.0:
			#tuplePlot+=(ListTotal[line][ListTotal[0].index('SigmaT')],ListTotal[line][ListTotal[0].index(float(184.5))])
			#PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaT')])]
			#PlotY+=[float(ListTotal[line][ListTotal[0].index(float(184.5))])]
	#plt.scatter(PlotX, PlotY, color='r', marker='o', alpha=0.6,s=120,label='184.5' )		
	#print(tuplePlot)
	
	
		plt.xticks(rotation=45,size = 13)
		plt.yticks(size =13)
		plt.title('SigmaT_8.0',fontsize = 18)
		plt.xlabel('sigmaF',fontsize = 15)
		plt.ylabel('snr',fontsize = 15)
		plt.legend(fontsize=10)
		plt.grid()
		plt.show()
	
	if modePlot=='2D_Color_ST_SF':
		maximum = [0,0,0]#[x,y,z]
		plt.figure()
		List = ['cmd_nbr_bonne_detection']
		if rapport: Det= 'cmd_nbr_detection' 
		if modeCalcul == 'SNR':
			List = ['cmd_somme_bonne_detection_snr']
			if rapport: Det= 'cmd_somme_total_snr' 
		for value in List:
			ListT=[]
			ListF=[]
			PlotT=[]
			PlotF=[]
			PlotZ=[]
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t=ListPlot[line,ListTotal[0].index('SigmaT')]
				f=ListPlot[line,ListTotal[0].index('SigmaF')]
				if float(t) not in ListT:
					ListT+= [float(t)]
				if float(f) not in ListF:
					ListF+= [float(f)]
					
			ListT.sort()
			ListF.sort()
			PlotT, PlotF = np.meshgrid(ListT, ListF)
			print(PlotT,PlotF)
			PlotZ = np.zeros_like(PlotT)
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t = ListPlot[line,ListTotal[0].index('SigmaT')]
				f = ListPlot[line,ListTotal[0].index('SigmaF')]
				if rapport: ## Uniquement pour cmb_nbr_detection et cmd_nbr_bonne_detection
					if ListTotal[line][ListTotal[0].index(Det)] is None: PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					elif ListTotal[line][ListTotal[0].index(Det)] =="": PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					elif ListTotal[line][ListTotal[0].index(Det)] == 0 or ListTotal[line][ListTotal[0].index(Det)] == '0' : PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					else : PlotZ[ListF.index(float(f)),ListT.index(float(t))]=100*float(ListPlot[line,ListTotal[0].index(value)])/(float(ListTotal[line][ListTotal[0].index(Det)])-float(ListPlot[line,ListTotal[0].index(value)]))
				else :
					if ListPlot[line,ListTotal[0].index(value)] is None:PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					else : PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(ListPlot[line,ListTotal[0].index(value)])
				if maximum[2] < PlotZ[ListF.index(float(f)),ListT.index(float(t))]:
					maximum = [float(f),float(t), PlotZ[ListF.index(float(f)),ListT.index(float(t))]]
					
		
		h = plt.contourf(PlotT, PlotF, PlotZ,cmap='viridis',levels=50)
		plt.axis('scaled')

		plt.colorbar()
		plt.xticks(size = 13)
		plt.yticks(size =13)
		if rapport : 
			if modeCalcul =='SNR':
				plt.title('SommeOfPourcentageSnr',fontsize = 18)
			else : plt.title('PourcentageOfDetection',fontsize = 18)
		else : 
			if modeCalcul =='SNR':
				plt.title('SommeGoodSNr',fontsize = 18)
			else : plt.title('Nbr of hits',fontsize = 18)
		plt.xlabel('SigmaT',fontsize = 15)
		plt.ylabel('SigmaF',fontsize = 15)
		plt.legend(fontsize=10)
		plt.grid()
		print('maximum',maximum)
		plt.show()
		
	
	
		#plt.xticks(rotation=45,size = 13)
		#plt.yticks(size =13)
		#plt.title('SigmaT_8.0',fontsize = 18)
		#plt.xlabel('sigmaF',fontsize = 15)
		#plt.ylabel('snr',fontsize = 15)
		#plt.legend(fontsize=10)
		#plt.grid()
		#plt.show()

	if modePlot=='2D_Color_BT_BF':
		maximum = [0,0,0]#[x,y,z]
		plt.figure()
		List = ['cmd_nbr_bonne_detection']
		if rapport: Det= 'cmd_nbr_detection' 
		for value in List:
			ListT=[]
			ListF=[]
			PlotT=[]
			PlotF=[]
			PlotZ=[]
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t=ListPlot[line,ListTotal[0].index('SigmaT')]
				f=ListPlot[line,ListTotal[0].index('SigmaF')]
				if float(t) not in ListT:
					ListT+= [float(t)]
				if float(f) not in ListF:
					ListF+= [float(f)]
					
			ListT.sort()
			ListF.sort()
			PlotT, PlotF = np.meshgrid(ListT, ListF)
			print(PlotT,PlotF)
			PlotZ = np.zeros_like(PlotT)
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t = ListPlot[line,ListTotal[0].index('SigmaT')]
				f = ListPlot[line,ListTotal[0].index('SigmaF')]
				if rapport: ## Uniquement pour cmb_nbr_detection et cmd_nbr_bonne_detection
					if ListTotal[line][ListTotal[0].index(Det)] is None: PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					elif ListTotal[line][ListTotal[0].index(Det)] =="": PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					elif ListTotal[line][ListTotal[0].index(Det)] == 0 or ListTotal[line][ListTotal[0].index(Det)] == '0' : PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(0)
					else : PlotZ[ListF.index(float(f)),ListT.index(float(t))]=100*float(ListPlot[line,ListTotal[0].index(value)])/(float(ListTotal[line][ListTotal[0].index(Det)])-float(ListPlot[line,ListTotal[0].index(value)]))
				else :
					PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(ListPlot[line,ListTotal[0].index(value)])
				if maximum[2] < PlotZ[ListF.index(float(f)),ListT.index(float(t))]:
					maximum = [float(f),float(t), PlotZ[ListF.index(float(f)),ListT.index(float(t))]]
					
		
		h = plt.contourf(PlotT, PlotF, PlotZ,cmap='viridis')
		plt.axis('scaled')

		plt.colorbar()
		plt.xticks(size = 13)
		plt.yticks(size =13)
		if rapport : plt.title('PourcentageOfDetection',fontsize = 18)
		else : plt.title('Nbr of hits',fontsize = 18)
		plt.xlabel('SigmaT',fontsize = 15)
		plt.ylabel('SigmaF',fontsize = 15)
		plt.legend(fontsize=10)
		plt.grid()
		print('maximum',maximum)
		plt.show()
		
	
	
		#plt.xticks(rotation=45,size = 13)
		#plt.yticks(size =13)
		#plt.title('SigmaT_8.0',fontsize = 18)
		#plt.xlabel('sigmaF',fontsize = 15)
		#plt.ylabel('snr',fontsize = 15)
		#plt.legend(fontsize=10)
		#plt.grid()
		#plt.show()
	if modePlot =='3D_observation':
		fig = plt.figure()
		ax = plt.axes(projection='3d')
		#zline = np.linspace(0, 100)
		#xline = ListSF
		#yline = ListST
		#ax.plot3D(xline, yline, zline, 'gray')
		if rapport : Det = 'cmd_nbr_detection' 
		List = ['cmd_nbr_bonne_detection']
		if SinglePulseSearch : List = [2349.8,184.5,2676.4,603.3,172.4,2155.3,1140.6,1623.0,2683.5,169.6,1617.9,586.1,2356.8,218.1,1793.8,1675.2,825.6,403.9,203.1,1690.9]
		for value in List:
			PlotX=[]
			PlotY=[]
			PlotZ=[]
			for line in range(1,len(ListPlot[:,0])):
				z= ListTotal[line][ListTotal[0].index(value)]
				if z is None:PlotZ+=[-10.00]
				elif z =="":
					PlotZ+=[-10.00]
				else : 
					if rapport : ## Uniquement pour cmb_nbr_detection et cmd_nbr_bonne_detection
						if ListTotal[line][ListTotal[0].index(Det)] is None: PlotZ+=[-0.00]
						elif ListTotal[line][ListTotal[0].index(Det)] =="": PlotZ+=[-1.00]
						elif ListTotal[line][ListTotal[0].index(Det)] == 0 or ListTotal[line][ListTotal[0].index(Det)] == '0' : PlotZ+=[-1.00]
						else : 
							print("DEBUG",z,"               ",ListTotal[line][ListTotal[0].index(Det)])
							PlotZ+=[100*float(z)/(float(ListTotal[line][ListTotal[0].index(Det)])-float(z))]
					else :  
						PlotZ+=[float(z)]
				PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaF')])]
				PlotY+=[float(ListTotal[line][ListTotal[0].index('SigmaT')])]
				
				#print(PlotX,'PlotX,'+str(len(PlotX))+'\n',PlotY,'PlotY,'+str(len(PlotY))+'\n',PlotZ,'PlotZ,'+str(len(PlotZ))+'\n')
			ax.scatter3D(np.array(PlotX), np.array(PlotY), np.array(PlotZ),label=value)
		#plt.title('3D plan for  Metaparameter :, DM search : ModeResearch :',fontsize = 18)
		#ax.set_xlabel('SigmaF Variation')
		#ax.set_ylabel('SigmaT Variation')
		ax.set_xlabel('SigmaF',fontsize = 25)
		ax.set_ylabel('SigmaT',fontsize = 25)
		if SinglePulseSearch : ax.set_zlabel('Signal Noise Ration',fontsize = 25) 
		elif rapport : ax.set_zlabel('% good detection')
		else : ax.set_zlabel('Hit nbr')
		plt.legend(fontsize=10)
		plt.grid()
		plt.show()
	
	if modePlot =='3D_Ontn':
		fig = plt.figure()
		ax = plt.axes(projection='3d')
		
		#zline = np.linspace(0, 100)
		#xline = ListSF
		#yline = ListST
		#ax.plot3D(xline, yline, zline, 'gray')
		
		PlotX=[]
		PlotY=[]
		PlotZ=[]
		value = 2349.8
		for line in range(1,len(ListPlot[:,0])):
			z= ListTotal[line][ListTotal[0].index(value)]
			if z is None:PlotZ+=[-10.00]
			elif z =="":
				PlotZ+=[-10.00]
			else : PlotZ+=[float(z)]
			PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaF')])]
			PlotY+=[float(ListTotal[line][ListTotal[0].index('SigmaT')])]
				
			print(PlotX,'PlotX,'+str(len(PlotX))+'\n',PlotY,'PlotY,'+str(len(PlotY))+'\n',PlotZ,'PlotZ,'+str(len(PlotZ))+'\n')
		ax.plot_surface(np.array(PlotX), np.array(PlotY), np.array(PlotZ))
		plt.title('3D plan for '+PathFileFits.split('_')[0]+', Metaparameter :, DM search :'+strDM+' ModeResearch :'+ModeResearch+'',fontsize = 18)
		ax.set_xlabel('SigmaF Variation')
		ax.set_ylabel('SigmaT Variation')
		ax.set_zlabel('Signal Noise Ration');

		plt.legend(fontsize=10)
		plt.grid()
		plt.show()
		# Data for a three-dimensional line
		#zline = np.linspace(0, 15, 1000)
		#xline = np.sin(zline)
		#yline = np.cos(zline)
		#ax.plot3D(xline, yline, zline, 'gray')

		# Data for three-dimensional scattered points
		#zdata = 15 * np.random.random(100)
		#xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
		#ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
		#ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
	if modePlot == '3D_Special':
		plt.figure()
		rapport=True
		List = ['cmd_nbr_bonne_detection']
		#if rapport : Det = 'cmd_nbr_detection' 
		for value in List:
			ListT=[]
			ListF=[]
			PlotT=[]
			PlotF=[]
			PlotZ=[]
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t=ListPlot[line,ListTotal[0].index('SigmaT')]
				f=ListPlot[line,ListTotal[0].index('SigmaF')]
				if float(t) not in ListT:
					ListT+= [float(t)]
				if float(f) not in ListF:
					ListF+= [float(f)]
					
			ListT.sort()
			ListF.sort()
			PlotT, PlotF = np.meshgrid(ListT, ListF)
			print(PlotT,PlotF)
			PlotZ = np.zeros_like(PlotT)
			for line in range(1,len(ListPlot[:,ListTotal[0].index('SigmaT')])):
				t = ListPlot[line,ListTotal[0].index('SigmaT')]
				f = ListPlot[line,ListTotal[0].index('SigmaF')]
				PlotZ[ListF.index(float(f)),ListT.index(float(t))]=float(ListPlot[line,ListTotal[0].index(value)])
		
			
			#for line in range(1,len(ListPlot[:,0])):
			#	z= ListTotal[line][ListTotal[0].index(value)]
			#	if z is None:PlotZ+=[-10.00]
			#	elif z =="":
			#		PlotZ+=[-10.00]
			#	else : 
			#		if rapport : ## Uniquement pour cmb_nbr_detection et cmd_nbr_bonne_detection
			#			if ListTotal[line][ListTotal[0].index(Det)] is None: PlotZ+=[-0.00]
			#			elif ListTotal[line][ListTotal[0].index(Det)] =="": PlotZ+=[-1.00]
			#			elif ListTotal[line][ListTotal[0].index(Det)] == 0 or ListTotal[line][ListTotal[0].index(Det)] == '0' : PlotZ+=[-1.00]
			#			else : 
			#				PlotZ+=[100*float(z)/(float(ListTotal[line][ListTotal[0].index(Det)])-float(z))]
			#		else :  
			#			PlotZ+=[float(z)]
			#	PlotX+=[float(ListTotal[line][ListTotal[0].index('SigmaF')])]
			#	PlotY+=[float(ListTotal[line][ListTotal[0].index('SigmaT')])]
			#plt.scatter(PlotX, PlotY, marker='o', alpha=0.6,s=120,label=str(value))
		#PlotZ
		
		ax = plt.axes(projection='3d')
		#ax.contour3D(PlotT,PlotF,PlotZ, 50, cmap='binary')
		ax.plot_surface(PlotT,PlotF,PlotZ, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
		ax.set_title('surface')
		ax.set_xlabel('PlotT')
		ax.set_ylabel('PlotF')
		ax.set_zlabel('PlotZ')
		plt.show()
		#ax = plt.axes(projection='3d')
		#ax.plot_wireframe(PlotT,PlotF,PlotZ,color='black')
		#ax.set_xlabel('x')
		#ax.set_ylabel('y')
		#ax.set_zlabel('z');
		#plt.show()

