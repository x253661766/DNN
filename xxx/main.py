from __future__ import print_function
import cPickle
import numpy
import random
from math import *
import sys
import pylab
from PIL import Image
import matplotlib.pyplot as pyplot
import re
from Pybh import *
from readTraj import *
from write import *
class TrajToImage:
	def __init__(self):
		self = self
	def toImage(self,eachtraj,wp,hp,wm,hm,t):
		Image = numpy.zeros((wm,hm),dtype = 'int32')	
		centerlat = 0.0
		centerlng = 0.0
		minlat = 400.0
		minlng = 400.0
		eachtrajlength = len(eachtraj)
		print (eachtrajlength)
		for i in range(0,eachtrajlength):
			centerlat = centerlat + float(eachtraj[i][0])
			centerlng = centerlng + float(eachtraj[i][1])
			if(float(eachtraj[i][0]) < minlat):
				minlat = float(eachtraj[i][0])
			if(float(eachtraj[i][1]) < minlng):
				minlng = float(eachtraj[i][1])
		centerlng = centerlng / eachtrajlength
		centerlat = centerlat /eachtrajlength
		offsetlng = floor(wm/2) - floor((centerlng - minlng) * wm/wp)
		offsetlat = floor(hm/2) - floor((centerlat - minlat) * hm/hp)
		for i in range(0,eachtrajlength):
			x = floor((float(eachtraj[i][1]) - minlng) * wm /wp) + offsetlng
			y = floor((float(eachtraj[i][0]) - minlat) * hm /hp) + offsetlat
			if   wm > x >= 0  and hm > y >= 0:
				Image[x][y] = Image[x][y] + 1
		return Image
if __name__ == '__main__':
	tti = TrajToImage()
	traj = readTraj()
	print (traj)

	image = tti.toImage(traj,0.2,0.2,40,40,2)
	numpy.set_printoptions(threshold='nan')
	print (image)
	writeImage(image)
	pyplot.imshow(image)
	pyplot.show()
	pyimage = Pybh()
	py_image = pyimage.pybhing(image,40,40,'3')
	writePyImage(py_image)
	print (py_image) 
	pyplot.imshow(py_image)
	pyplot.show()
