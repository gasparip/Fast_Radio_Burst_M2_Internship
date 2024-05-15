import numpy as np
import psrchive as psr
import pyfits as fi
import psrfits as pf
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import argparse as arg

parser = arg.ArgumentParser(description='transforme 32 bits data to a flatband 8 bits without scales and offsets.')

parser.add_argument('-f', dest='fileName', type=str, help='Name of the FITS file to change.')

args = parser.parse_args()
## Observation 
DocumentName=args.fileName

## Observation 
#DocumentName='/data/pgaspari/ParametreOptimisation/Dir_Simu_Fits/13sommes_TimeDiff10.fits'
#fi.info(DocumentName)
FileFits = pf.Arch(DocumentName)
FileFits.Dyn_spec_structure()
ArrayTF = FileFits.data
#print(FileFits.tsample)
### Plot Observation

ListF=np.linspace(FileFits.lofreq,FileFits.hifreq,len(ArrayTF[0]))
ListT=np.linspace(0,FileFits.Tobs,len(ArrayTF[:,0]))
NormArrayTF = np.zeros([len(ListT)])
FreqAmplobs = []

for i in range(len(ListF)):
	FreqAmplobs+=[sum(ArrayTF[:,i])/len(ArrayTF[:,i])]
	#NormArrayTF[:,i] = ArrayTF[:,i] - (sum(ArrayTF[:,i])/len(ArrayTF[:,i]))/np.std(ArrayTF[:,i])
	
	
TempsAmplobs = []
#TempsAmplNorm =[]
#TempsAmplNorm =[]
for j in range(len(ListT)):
	TempsAmplobs+=[sum(ArrayTF[j,:])/len(ArrayTF[j,:])]
	#TempsAmplNorm+= ArrayTF[j,:] - (sum(ArrayTF[j,:])/len(ArrayTF[j,:]))/np.std(ArrayTF[j,:])

fig = plt.figure(8,6)
gs = GridSpec(2,3,figure=fig)
axs2 = fig.add_subplot(gs[1,:-1])
axs1 = fig.add_subplot(gs[0,:-1],sharex=axs2)
axs3 = fig.add_subplot(gs[1,-1],sharey=axs2)

axs2.pcolormesh(ListT, ListF ,ArrayTF.T)
axs2.set_xlabel('Time(s)',fontsize = 20)
axs2.set_xlim((ListT[0],ListT[-1]))
axs2.set_ylim((ListF[0],ListF[-1]))
axs2.set_ylabel('Frequency(MHz)',fontsize = 20)
#axs[0,0].colorbar()

plt.setp(axs3.get_yticklabels(), visible=False)
#axs[0,0].colorbar()
axs3.plot(FreqAmplobs,ListF)
axs3.set_xlabel('Amplitude',fontsize = 1518)
axs3.set_ylim((ListF[0],ListF[-1]))
ax4=axs3.twiny()
ax4.set_ylim([0, 191])
ax4.set_ylabel('Channel Number')
axs3.grid()

plt.setp(axs1.get_xticklabels(), visible=False)
axs1.plot(ListT,TempsAmplobs)
axs1.set_ylabel('Amplitude',fontsize = 20)
axs1.set_xlim((ListT[0],ListT[-1]))
axs1.grid()
plt.tight_layout()
plt.show()





