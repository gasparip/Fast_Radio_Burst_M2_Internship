import numpy as np
import matplotlib.pyplot as plt
SizePulse=False
if SizePulse : ToDoFile='/data/pgaspari/Simulation/DirTestSimu/TestParametreSimulation/FileToPython.txt'
else :ToDoFile='/data/pgaspari/Simulation/DirTestSimu/TestParametreSimulation/FileToPython.txt'
ToDoFileExec = open(ToDoFile,"r")
linesObs = ToDoFileExec.readlines()
ToDoFileExec.close()

BoolHeader=True
ListBlocks05=[]
ListBlocks1=[]
ListBlocks2=[]
ListBlocks4=[]
ListBlocks8=[]
ListBlocks16=[]

for line in linesObs:
	NewLine=line.replace('\n','')
	if NewLine[0:10]=='Simulation' and BoolHeader == True:
		BoolHeader=False
		print('In Header')
	
		Split1=NewLine.split('E')[1]
		Split2=Split1.split('D')
		energy = float(Split2[0][1:-1].replace('_','.'))
		Split3=Split2[1].split('B')
		Duration=float(Split3[0][1:-1].replace('_','.'))
		Blocks=Split3[1].split('.')[0][1:]
		print(Blocks)
		if Blocks == '0':
			Blocks='05'
		print(NewLine,energy,Duration,Blocks)
	elif BoolHeader==False:
		BoolHeader = True
		if SizePulse: 
			if NewLine != 'VIDE' and energy==float(2):
				print('nonvide')
				Data=NewLine.split()
				print(Data)
				SNR=float(Data[1])
				if Blocks == '05':
					ListBlocks05+=[[energy,Duration*2,SNR]]
				if Blocks == '1':
					ListBlocks1+=[[energy,Duration*2,SNR]]
				if Blocks == '2':
					ListBlocks2+=[[energy,Duration*2,SNR]]
				if Blocks == '4':
					ListBlocks4+=[[energy,Duration*2,SNR]]
				if Blocks == '8':
					ListBlocks8+=[[energy,Duration*2,SNR]]
				if Blocks == '16':
					ListBlocks16+=[[energy,Duration*2,SNR]]
			else : 
				print('vide')
		else:
			if NewLine != 'VIDE' and energy!=float(4) and energy!=float(5):
				print('nonvide')
				Data=NewLine.split()
				print(Data)
				SNR=float(Data[1])
				if Blocks == '05':
					ListBlocks05+=[[energy,Duration*2,SNR]]
				if Blocks == '1':
					ListBlocks1+=[[energy,Duration*2,SNR]]
				if Blocks == '2':
					ListBlocks2+=[[energy,Duration*2,SNR]]
				if Blocks == '4':
					ListBlocks4+=[[energy,Duration*2,SNR]]
				if Blocks == '8':
					ListBlocks8+=[[energy,Duration*2,SNR]]
				if Blocks == '16':
					ListBlocks16+=[[energy,Duration*2,SNR]]
			else : 
				print('vide')
ListBlocks05=np.array(ListBlocks05)
ListBlocks1=np.array(ListBlocks1)
ListBlocks2=np.array(ListBlocks2)
ListBlocks4=np.array(ListBlocks4)
ListBlocks8=np.array(ListBlocks8)
ListBlocks16=np.array(ListBlocks16)
print(ListBlocks05)
#for i in range(5):
	
#	plt.scatter(plotX, Yplot[i], color='r', marker='x')
if SizePulse:i = 1
else : i=0
j = 2


fig, ax = plt.subplots(figsize = (12, 8))
#ax.scatter(x, y, s=60, alpha=0.7, edgecolors="k")
ax.set_xscale("log")
ax.scatter(ListBlocks05[:,i],ListBlocks05[:,j],color='y',label='Blocks : 20.8s')
ax.scatter(ListBlocks1[:,i],ListBlocks1[:,j],color='m',label='Blocks : 10.4s')
ax.scatter(ListBlocks2[:,i],ListBlocks2[:,j],color='g',label='Blocks : 5.2s')
ax.scatter(ListBlocks4[:,i],ListBlocks4[:,j],color='c',label='Blocks : 2.6s')
ax.scatter(ListBlocks8[:,i],ListBlocks8[:,j],color='b',label='Blocks : 1.3s')
ax.scatter(ListBlocks16[:,i],ListBlocks16[:,j],color='k',label='Blocks : 0.7s')
plt.tick_params(axis = 'both', labelsize = 14)
plt.xlim(left=0.08,right=60)
plt.title('FRB20220912A, SNR as functon of Burst Amplitude',fontsize = 20)
if SizePulse:plt.xlabel('Burst Width(s)',fontsize = 20)
else :plt.xlabel('Burst Amplitude',fontsize = 20)
plt.ylabel('SNR',fontsize = 20)
plt.legend(fontsize = 20)
plt.show()
# Set logarithmic scale on the both variables

