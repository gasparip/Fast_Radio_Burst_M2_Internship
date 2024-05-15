import argparse
import matplotlib.pyplot as plt
import numpy as np
parser = argparse.ArgumentParser( 'Script to apply a rfifind mask.' )
parser.add_argument( dest='filename' , type=str , help='Filename' )
args = parser.parse_args()

FichierRfi = open(args.filename,"r")
linesRFI= FichierRfi.readlines()
FichierRfi.close()

header=[]
headerDone=True
ListCandidate=[]
badList=[]


compteur1=0
compteur2=0
for ligne in linesRFI:
	Candidat=[]
	badListCandiate=[]
	ligne=ligne.replace('\n','')
	ligne=ligne.replace('(','')
	ligne=ligne.replace(')','')
	ligne=ligne.replace('[','')
	ligne=ligne.replace(']','')
	ligne=ligne.replace('\'','')
	if ligne =='' or ligne ==' ':
		print('manque des infos')
	else:
		ArgumentLigne=ligne.split()
		print(ArgumentLigne)
		#print('hello',ArgumentLigne[0].split(':'))
		#print(ArgumentLigne)
		if ArgumentLigne[0].split(':')[0] == 'ObsName':
			print("On rentre ObsName")
			for i in range(len(ArgumentLigne)):
				info=ArgumentLigne[i].split(':')
				Candidat+=[info[1]]
				#print(info)
				if headerDone:
					header+=[info[0]]
			if headerDone:
				headerDone=False
			ListCandidate+=[Candidat]
			compteur1+=1
			print(compteur1)
		elif ArgumentLigne[0] =='bad_clm:' or  ArgumentLigne[0] =='Nothing' :
			if  ArgumentLigne[0] =='Nothing':
				print('Nothing')
				badListCandiate+=[False]
				badList+=[badListCandiate]
			else :
				print("On rentre bad_clm")
				ligneBadclm=(ligne.replace(' ','')).split(',')
				#print(ligneBadclm)
				print(ligneBadclm)
				for i in range(1,len(ligneBadclm)):
					badListCandiate += [int(ligneBadclm[i])]
				badList+=[badListCandiate]
			compteur2+=1
			print(compteur2)
		else :
			print('Probleme')
if len(ListCandidate) != len(badList):
	print('!!!!!!!!!!!!!!!!!!!!!!!!!! Problem !!!!!!!!!!!!!!!!!!!!')
print('header',header)
print(len(ListCandidate),'ListCandidate',ListCandidate)
print(len(badList),'badListCandiate',badList)
plt.figure()
arrayNumpy=np.array(ListCandidate)
ma_liste = arrayNumpy[:,1]
indices_tries = sorted(range(len(ma_liste)), key=lambda k: ma_liste[k])
floattosoust=0.3
print(ListCandidate[indices_tries[216]])
for i in range(len(ListCandidate)):
	if (int(ma_liste[indices_tries[i]].split('T')[1][0:2]) >= 18 or int(ma_liste[indices_tries[i]].split('T')[1][0:2]) <= 4):
		coulor='k'
	else:
		coulor='r'
	x=[i]*len(badList[indices_tries[i]])
	xmin=[i-floattosoust]*len(badList[indices_tries[i]])
	xmax=[i+floattosoust]*len(badList[indices_tries[i]])
	y=badList[indices_tries[i]]
	#plt.scatter(x, y,color='k',s=10, linewidths=10)
	#plt.scatter(x, y,30,color='k', marker=r'$--$')
	plt.hlines(y,xmin,xmax,color=coulor)
plt.show()

f, (ax,ax2) = plt.subplots(1,2, gridspec_kw={'width_ratios':[3,1]}, figsize=(10,8), sharey=True)
plt.subplots_adjust(wspace=0.15)
floattosoust=0.3
#for i in range(len(ListCandidate)):
for i in range(210):	
	print(i,'     ',ma_liste[indices_tries[i]])
	if (int(ma_liste[indices_tries[i]].split('T')[1][0:2]) >= 19 or int(ma_liste[indices_tries[i]].split('T')[1][0:2]) <= 8):
		coulor='k'
	else:
		coulor='r'
	x=[i]*len(badList[indices_tries[i]])
	xmin=[i-floattosoust]*len(badList[indices_tries[i]])
	xmax=[i+floattosoust]*len(badList[indices_tries[i]])
	y=badList[indices_tries[i]]
	#plt.scatter(x, y,color='k',s=10, linewidths=10)
	#plt.scatter(x, y,30,color='k', marker=r'$--$')
	ax.hlines(y,xmin,xmax,color=coulor)

#position=np.linspace(0,191,192,dtype=int)
#labels=np.linspace(44.921875,82.2256562,192,dtype=str)
#print(position)
#print(labels)
ax.set_ylim([-1, 193])
ax.set_ylabel('Channel Number')
ax.set_xlabel('Obs Number')
ax.grid()
#ax.set_yticks(position, labels)

ax3=ax.twinx()
ax3.set_ylim([45, 80])
ax3.set_ylabel('Frequency(MHz)')


Counts=[0]*192
#for i in range(len(badList)):
for i in range(210):
	for j in badList[indices_tries[i]]:
		Counts[int(j)]+=1
y=np.linspace(0,191,192)
hbars = ax2.barh(y,np.array(Counts)/float(210)*100)
#hbars = ax2.barh(y,np.array(Counts)/float(len(ListCandidate))*100)
ax2.set_ylim([-1, 193])
ax2.set_xlabel("Percentage Of RFI channel")
ax2.grid()
plt.show()






