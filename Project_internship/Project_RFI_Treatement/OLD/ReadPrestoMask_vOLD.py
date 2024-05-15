#import rfifind as rfi
import sys
#sys.path.append( '/home/mbrionne/.local/lib/python2.7' )
#import infodata
import numpy as np
import pylab as plt
import glob
#import filterbank as fil
import psrfits as pfi
import argparse


class rfifind(object):

	def __init__(self, filename):
		self.basename = filename.split('.')[0]
		self.infodata()

	def infodata (self) :
		filenm = self.basename+".inf"
		self.breaks = 0
		for line in open(filenm):
		    if line.startswith(" Data file name"):
		        self.basenm = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Telescope"):
		        self.telescope = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Instrument"):
		        self.instrument = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Object being observed"):
		        self.object = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" J2000 Right Ascension"):
		        self.RA = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" J2000 Declination"):
		        self.DEC = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Data observed by"):
		        self.observer = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Epoch"):
		        self.epoch = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Barycentered?"):
		        self.bary = int(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Number of bins"):
		        self.nsamp = int(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Width of each time series bin"):
		        self.dt = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Any breaks in the data?"):
		        self.breaks = int(line.split("=")[-1].strip())
		        if self.breaks:
		            self.onoff = []
		        continue
		    if line.startswith(" On/Off bin pair"):
		        vals = line.split("=")[-1].strip().split(",")
		        self.onoff.append((int(vals[0]), int(vals[1])))
		        continue
		    if line.startswith(" Type of observation"):
		        self.waveband = line.split("=")[-1].strip()
		        continue
		    if line.startswith(" Beam diameter"):
		        self.beam_diam = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Dispersion measure"):
		        self.DM = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Central freq of low channel"):
		        self.lofreq = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Total bandwidth"):
		        self.BW = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Number of channels"):
		        self.nchan = int(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Channel bandwidth"):
		        self.chan_width = float(line.split("=")[-1].strip())
		        continue
		    if line.startswith(" Data analyzed by"):
		        self.analyzer = line.split("=")[-1].strip()
		        continue

	def read_mask(self):

		x = open(self.basename+".mask")
		self.time_sig, self.freq_sig, self.MJD, self.dtint, self.lofreq, self.df = \
		               np.fromfile(x, dtype=np.float64, count=6)
		nchan, self.nint, self.ptsperint = np.fromfile(x, dtype=np.int32, count=3)

		self.times = np.arange(self.nint)*self.dtint
		self.MJDs = self.times/86400.0 + self.MJD
		self.freqs = np.arange(self.nchan)*self.df + self.lofreq

		nzap = np.fromfile(x, dtype=np.int32, count=1)[0]
		if nzap:
		    self.mask_zap_chans = np.fromfile(x, dtype=np.int32, count=nzap)
		else:
		    self.mask_zap_chans = np.asarray([])
		#if len(self.mask_zap_chans)==self.nchan:
		    #print("WARNING!:  All channels recommended for masking!")

		nzap = np.fromfile(x, dtype=np.int32, count=1)[0]
		if nzap:
		    self.mask_zap_ints = np.fromfile(x, dtype=np.int32, count=nzap)
		else:
		    self.mask_zap_ints = np.asarray([])
		#if len(self.mask_zap_ints)==self.nint:
		   # print("WARNING!:  All intervals recommended for masking!")

		nzap_per_int = np.fromfile(x, dtype=np.int32, count=self.nint)
		self.mask_zap_chans_per_int = []
		for nzap in nzap_per_int:
		    if nzap:
		        if nzap == nchan:
		            tozap = np.arange(0, nchan, dtype=np.int32)
		        else:
		            tozap = np.fromfile(x, dtype=np.int32, count=nzap)
		    else:
		        tozap = np.asarray([])
		    self.mask_zap_chans_per_int.append(tozap)
		x.close()

	def plot_mask (self) :

		maskArray = np.zeros( (self.nint , self.nchan) )
		maskArray[ self.mask_zap_ints , : ] = 1
		maskArray[ : , self.mask_zap_chans ] = 1
		for i in range( self.nint ) :
			maskArray[ i , self.mask_zap_chans_per_int[i] ] = 1
		#print "Zapped percentage : {:.3f} %".format( 100. * maskArray.sum() / ( self.nint * self.nchan ) )
		plt.figure( 'Rfifind mask' )
		plt.imshow( maskArray , aspect='auto' )
		plt.show()

	def apply_mask ( self , data ) :

		maskArray = np.zeros( (self.nint , self.nchan) )
		if self.mask_zap_ints.size > 0 :
			maskArray[ self.mask_zap_ints , : ] = 1
		if self.mask_zap_chans.size > 0 :
			maskArray[ : , self.mask_zap_chans ] = 1
		for i in range( self.nint ) :
			maskArray[ i , self.mask_zap_chans_per_int[i] ] = 1
		maskArray = maskArray.repeat( self.ptsperint , axis=0 )
		maskArray = np.fliplr( maskArray )

		if data.shape[0] < maskArray.shape[0] :
			maskArray = maskArray[ : data.shape[0] , : ]
#		maskedArray = np.ma.masked_array( data.copy() , maskArray )

		#print 'padval'
		self.determine_padvals()

		#print 'fill'
#		maskArray = maskArray * self.padvals
		np.place( data , maskArray , self.padvals )
#		for ichan in range( self.nchan ) :
#			maskedArray[:,ichan] = maskedArray[:,ichan].filled( self.padvals[ichan] )

		return data
		

	def determine_padvals(self, frac_to_keep=0.8):
		"""
		determine_padvals():
		    This routines determines padding values to use for each
		    channel.
		"""
		# NOTE: Casting to 64/32-bit floats are done to mimick 'mask.c'.
		self.read_stats()
		num = int(np.round(self.nint*frac_to_keep))
		start = (self.nint - num) // 2
#		self.padvals = np.zeros(self.nchan, dtype='float32')
		sortAvgStats = np.sort( self.avg_stats , 0 )[start:start+num]
		self.padvals = np.mean( sortAvgStats , 0 , dtype=np.uint8 )

	def read_stats(self):
		x = open(self.basename+".stats")
		self.nchan, self.nint, self.ptsperint, self.lobin, self.numbetween = \
		            np.fromfile(x, dtype=np.int32, count=5)
		count = self.nchan * self.nint
		self.pow_stats = np.fromfile(x, dtype=np.float32, count=count)
		self.avg_stats = np.fromfile(x, dtype=np.float32, count=count)
		self.std_stats = np.fromfile(x, dtype=np.float32, count=count)
		self.pow_stats.shape = (self.nint, self.nchan)
		self.avg_stats.shape = (self.nint, self.nchan)
		self.std_stats.shape = (self.nint, self.nchan)
		x.close()
	
	def bad_colomun(self):
		bad_colomun=[]
		maskArray = np.zeros( (self.nint , self.nchan) )
		if self.mask_zap_ints.size > 0 :
			maskArray[ self.mask_zap_ints , : ] = 1
		if self.mask_zap_chans.size > 0 :
			maskArray[ : , self.mask_zap_chans ] = 1
		for i in range( self.nint ) :
			maskArray[ i , self.mask_zap_chans_per_int[i] ] = 1
		maskArray = maskArray.repeat( self.ptsperint , axis=0 )
		#maskArray = np.fliplr( maskArray )
		maximumValue = len(maskArray[:,0])
		bad_colomun=[]
		for j in range(self.nchan):
			#print(sum(maskArray[:,j]))
			#print(self.nint*0.8)
			if sum(maskArray[:,j]) > maximumValue*0.8:
				bad_colomun += [j]
		#print(bad_colomun)
		if bad_colomun == []:
			print('Nothing')
		else:
			print('bad_clm: ',bad_colomun)

def write_masked_fbk ( Filename , Maskfile ) :

	#print 'Extracting data\n'
	if args.fbk :
		fbk = fil.FilterbankFile( Filename )
		spc0 = fbk.get_spectra()
		fbk.close()
	else :
		ar = pfi.Arch( Filename )
		ar.Dyn_spec_structure()
		spc0 = ar.data

	#print 'Reading mask\n'
	msk = rfifind( Maskfile )
	msk.read_mask()
	#print 'Applying of the mask\n'
	maskedData = msk.apply_mask( spc0 )
	

	#print "Writing of the new fbk\n"
	outName = Filename.split('.')[0]
	head_data , head_size = fil.read_header( Filename )
	fil.create_filterbank_file( '{:s}.masked.fbk'.format( outName ) , header=head_data , spectra=maskedData , verbose=True )


def plot_masked_fbk ( Filename , Maskfile ) :

	#print 'Extracting data\n'
	if args.fbk :
		fbk = fil.FilterbankFile( Filename )
		spc0 = fbk.get_spectra()
		t_obs = fbk.times[-1]
		f_min = fbk.frequencies[-1]
		f_max = fbk.frequencies[0]
		fbk.close()
		del fbk
	else :
		ar = pfi.Arch( Filename )
		ar.Dyn_spec_structure()
		t_obs = ar.Tobs
		f_min = ar.lofreq
		f_max = ar.hifreq
		spc0 = ar.data
		del ar

	#print 'Reading mask\n'
	msk = rfifind( Maskfile )
	msk.read_mask()
	#print 'Applying of the mask\n'
	#msk.plot_mask()
	if args.ReturnBadColomn:
		msk.bad_colomun()
	#maskedData = msk.apply_mask( spc0 )

	#plt.imshow( maskedData.transpose() , aspect='auto' , extent=[0.,t_obs,f_min,f_max] )
	#plt.xlabel( 'Times' )
	#plt.ylabel( 'Frequencies' )
	#plt.show()


if __name__ == '__main__' :

	parser = argparse.ArgumentParser( 'Script to apply a rfifind mask.' )
	parser.add_argument( dest='filename' , type=str , help='Filename' )
	parser.add_argument( '-m' , dest='maskname' , type=str , help='Name of the mask file.' )
	parser.add_argument( '--fil' , dest='fbk' , action='store_true' , help='For a filterbank file.' )
	parser.add_argument( '--fits' , dest='pfits' , action='store_true' , help='For a PSRFITS file.' )
	parser.add_argument( '-p' , dest='plot' , action='store_true' , help='Option to just plot the masked dynamic spectrum.' )
	parser.add_argument( '-w' , dest='write' , action='store_true' , help='Option to write a new filterbank file with the masked dynamic spectrum.' )
	parser.add_argument( '-t' , dest='ReturnBadColomn' , action='store_true' , help='return a file with bad colomun' )
	args = parser.parse_args()

	if args.plot :
		plot_masked_fbk( args.filename , args.maskname )

	if args.write :
		write_masked_fbk( args.filename , args.maskname )

'''plt.figure( figsize=(10,8) )
plt.subplot( 121 )
plt.imshow( spc0 , aspect='auto' )
plt.subplot( 122 )
plt.imshow( spc1 , aspect='auto' )
plt.show()'''
