# Module to open an archive in PSRFITS format
# Author: Mark BRIONNE
# Date: 24-03-2023

import numpy as np
import psrchive as psr
import pyfits as fi

class Arch :

	def __init__ ( self , fileName ) :

		print "\nExtraction of the data.\n"
		ar = psr.Archive_load( fileName )

		self.refDM = ar.get_dispersion_measure()
		self.cf = ar.get_centre_frequency()
		self.bw = ar.get_bandwidth()
		self.nchan = ar.get_nchan()

		try :
			subint0 = ar.get_Integration( 0 )
			self.Tint = subint0.get_folding_period()
			self.nbins = subint0.get_nbin()
			self.tsample = self.Tint / self.nbins
			del subint0

		except IndexError :
			h0 = fi.getheader( fileName , 1 )
			self.tsample = h0['tbin']
			self.nbins = h0['nsblk']
			self.Tint = self.tsample * self.nbins
			del h0

		self.bw_chan = ar.get_bandwidth() / ar.get_nchan()
		self.lofreq = self.cf - self.bw / 2. + self.bw_chan / 2.
		self.hifreq = self.cf + self.bw / 2. - self.bw_chan / 2.

		self.freqs = np.arange( self.lofreq , self.hifreq + self.bw_chan , self.bw_chan )
		self.times = np.arange( 0 , self.Tint , self.tsample )
		self.times += self.tsample / 2.

		self.data = ar.get_data().sum(1)			# Erase polarization
		if self.data.size == 0 :
			d0 = fi.getdata( fileName )
			dt0 = d0.field(16).squeeze()
			#dt0 =d0.field(16).sum(2).squeeze()		# Erase polarization
			dt0 = dt0[:,:,0,:]
			#dt0 = dt0[:,:,:]
			self.data = np.swapaxes( dt0 , 1 , 2 )
			del dt0

		self.weights = ar.get_weights()
		if self.weights.size == 0 :
			self.weights = d0.field(13)

		self.nsubint = self.data.shape[0]
		self.Tobs = self.Tint * self.nsubint

		self.flag_norm = False

		if self.data.size == 0 :
			del d0
		del ar


	def Dyn_spec_structure ( self ) :

		wts = self.weights.copy()
		wts = wts.repeat( self.nbins ).reshape( self.data.shape )
		wts = np.hstack( list( wts ) )
		self.weights = wts.transpose()

		dts = self.data.copy()
		dts = np.hstack( list( dts ) )
		self.data = dts.transpose()

		del wts
		del dts


	def Get_weighted_data ( self ) :

		return self.data * self.weights


	def Set_refDM ( self , newdm ) :

		print "\nSet a new reference DM at {:f} pc.cm^-3\n".format( newdm )
		self.refDM = newdm


	def Folding ( self ) :

		print "\nFolding of the data.\n"
		self.Subint_struct()
		dtf = self.data.copy()
		wtf = self.weights.copy()
		self.data = np.transpose( dtf.mean(0) )
		self.weights = np.transpose( wtf.mean(0) )
		del dtf
		del wtf


	def Norm_data ( self ) :

		if self.flag_norm :
			print "\nData are already normalized.\n"
		else :
			self.orig_stats = np.column_stack( ( self.data.mean(0) , self.data.std(0) ) )
			ndata = ( self.data - self.data.mean(0) ) / self.data.std(0)
			self.data = ndata.copy()
			self.flag_norm = True
			del ndata


	def Rescaled_data ( self ) :

		if self.flag_norm :
			odata = self.data * self.orig_stats[:,1] + self.orig_stats[:,0]
			self.data = odata.copy()
			self.flag_norm = False
			del odata
		else :
			print "Data are already in the original scale."


	def Subint_struct ( self ) :

	        if len( self.data.shape ) >= 3 :
	                print "There is already a subintegration structure."
	        else :
	                sdata = self.data.transpose()
	                sdata = np.hsplit( sdata , self.nsubint )
		        self.data = np.array( sdata )
