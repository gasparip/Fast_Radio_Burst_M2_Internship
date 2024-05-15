# -*- coding: utf-8 -*-
import numpy as np
import psrchive as psr
import pyfits as fi
import psrfits as pf
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting
import argparse as arg

DocumentName='./SimulationFRB20220912A_D_0_001_E_5.fits'
filename='/TestSimulationFRB20220912A_D_0_001_E_5.fits
#fi.info(DocumentName)
FileFits = pf.Arch(DocumentName)
FileFits.Dyn_spec_structure()
ArrayTF = FileFits.data
ListF=np.linspace(FileFits.lofreq,FileFits.hifreq,len(ArrayTF[0]))
ListT=np.linspace(0,FileFits.Tobs,len(ArrayTF[:,0]))
FreqAmplobs = []
mean=0
for i in range(len(ListF)):
	FreqAmplobs+=[sum(ArrayTF[:,i])/len(ArrayTF[:,i])]
	#NormArrayTF[:,i] = ArrayTF[:,i] - (sum(ArrayTF[:,i])/len(ArrayTF[:,i]))/np.std(ArrayTF[:,i])
mean=sum(FreqAmplobs[:])/len(FreqAmplobs)
print(mean)
print(len(FreqAmplobs))
for i in range(len(ListF)):
	print(i)
	if FreqAmplobs[i] >= 2*mean :
		ArrayTF[:,i]=[False]*len(ArrayTF[:,i])
	ArrayTF[:,i]=[0]*len(ArrayTF[:,i])
FileFits.data=ArrayTF
FileFits.Subint_struct()

NewArray=[]
NewArray = np.swapaxes(FileFits.data,1,2)
data = fi.getdata(DocumentName)
print(data.shape)
dataArray=data.field(16)
dataCol=data.columns[16].copy()  
dataArray[:,:,0,:,0]=NewArray
colList = []        

        # Field list for the new fits file
for i in range(16):
	oldArray = data.field(i)                   # Copy of the old amplitude data array
	oldCol = data.columns[i].copy() 
	newCol = fi.Column(name=oldCol.name,         # Creation of the new field
		format=oldCol.format,
		unit=oldCol.unit,
		dim=oldCol.dim,
		array=oldArray)    
	colList.append(newCol)

newCol = fi.Column(name=dataCol.name,         # Creation of the new field
		format=dataCol.format,
		unit=dataCol.unit,
		dim=dataCol.dim,
		array=dataArray)    
colList.append(newCol)

headObs = fi.getheader(DocumentName, 0, do_not_scale_image_data=True, scale_back=True)        
head = fi.getheader(DocumentName, 1, do_not_scale_image_data=True, scale_back=True) 


colDefs = fi.ColDefs(colList)                    # Creation of the new fields object
tbhdu = fi.BinTableHDU.from_columns(colDefs, header=head)    # Creation of the new data table object

prihdu = fi.PrimaryHDU(header=headObs)            # Creation of the new observation header (exactly the same that the old fits file)
hdulist = fi.HDUList([prihdu, tbhdu])            # Creation of the new HDU object

hdulist.writeto(filename)  # output_verify='exception' )                # Writing the new HDU object on the new fits file
hdulist.close()
