import numpy as np
import multiprocessing as mp
import argparse
import os
import subprocess
import pyfits as fi
import sys


# Input parameters

parser = argparse.ArgumentParser( description='Creation of the dedispersion plan used by prepsubband.' )
parser.add_argument( dest='file' , type=str , help='Name of the filterbank file to use.' )
parser.add_argument( '-s' , '--dmstep' , default=0.01 , type=float , help='DM step to use (default = 0.01 pc.cm-3).' )
parser.add_argument( '-d' , '--ds' , default=1 , type=int , help='Downsampling to use (default = 1).')
parser.add_argument( '-m' , '--dmmax' , type=float , default=300.0 , help='Maximal DM  to use for the research (default = 300.0 pc.cm-3).' )
## Pierre Modify
parser.add_argument( '-min' , '--dmmin' , type=float , default=0.0 , help='Minimal DM  to use for the research (default = 300.0 pc.cm-3).' )
## End Pierre Modify
parser.add_argument( '-n' , '--nb' , type=int , default=1000 , help='Maximal number of DM to try for a given downsampling (default = 1000).' )
parser.add_argument( '-c' , '--cpus' , type=int , default=40 , help='Number of cores to use (default = 30).' )
parser.add_argument( '-k' , '--mask', type=str , help='Name of the mask file to use.' )
parser.add_argument( '-o' , '--out', type=str , help="Name of the DD plan outfile to create." )
args = parser.parse_args()


# Functions

def fbkInfo ( fbkFile ) :

	infoFile = open( fbkFile.split('.')[0] + '.readfile' , 'r' )

	for line in infoFile.readlines() :
		if line.find( 'Sample time' ) != -1 :
			tsamp = float( line.split('=')[1] )
		elif line.find( 'Low channel' ) != -1 :
			lowfreq = float( line.split('=')[1] )
		elif line.find( 'Channel width' ) != -1 :
			bwchan = float( line.split('=')[1] )
		elif line.find( 'Number of channels' ) != -1 :
			nchan = float( line.split('=')[1] )
		elif line.find( 'Spectra per subint' ) != -1 :
			spc = float( line.split('=')[1] )

	infoFile.close()

	return tsamp * 1e-6 , lowfreq , bwchan , nchan , spc


# Adjusting the number of CPUs to use

if mp.cpu_count() < args.cpus :
	args.cpus = mp.cpu_count()
else :
	args.cpus = args.cpus


# Adjusting the number of DM to try by CPU and the DM step

if args.nb > 1000 :
	args.nb = 1000

nDM_cpu = int( round ( (args.dmmax-args.dmmin) / args.dmstep / args.cpus , 0 ) )

if nDM_cpu > args.nb :
	if nDM_cpu <= 1000 :
		args.nb = nDM_cpu
	else :
		args.dmstep = round( (args.dmmax-args.dmmin)/ ( 1000 * args.cpus ) , 2 ) ## Modify by pierre
		nDM_cpu = int( round( (args.dmmax -args.dmmin)/ ( args.dmstep * args.cpus ) , 0 ) ) ## Modify by pierre


# Low DM vector computing

loDM = [ args.dmmin + i * args.dmstep * nDM_cpu for i in range( args.cpus ) ] ## Modify by pierre
#loDM = loDM[-10:]
#print "loDM", loDM
#raw_input("Press Enter to continue...")
#exit

# Downsampling and number of subbands computing



s=1
d=192
# Write the DD plan in an ASCII file

if args.out :

	print "\n\tWriting DD plan in the file :\t'{:s}.ddplan'.\n".format( args.out )

	_file0 = open( args.out + '.ddplan' , 'w' )
	for l in loDM :
        	_file0.write( "{:.4f}\t{:.4f}\t{:d}\t{:d}\t{:d}\n".format( l , args.dmstep , s , d , nDM_cpu ) )

	_file0.close()
