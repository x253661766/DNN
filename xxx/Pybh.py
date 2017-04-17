import cv2
import numpy as np
import matplotlib.pyplot as plt
import cPickle
import numpy
import pylab
class Pybh:
	def __init__(self):
		self = self
	def pybhing(self,image,Wm,Hm,cnt):
		if(cnt == '1'):
			img = image.reshape(Wm,Hm)
			rows,cols = img.shape
			mask = np.ones(img.shape,np.uint8)
			mask[rows/2-15:rows/2+15,cols/2-15:cols/2+15] = 0
			f = np.fft.fft2(img)
			fshift = np.fft.fftshift(f)
			fshift = fshift*mask
			f2shift = np.fft.ifftshift(fshift)
			img_new = np.fft.ifft2(f2shift)
			s1 = np.abs(img_new)
			return numpy.ndarray.flatten(s1).reshape(Wm,Hm)
		elif(cnt == '2'):
			img = image.reshape(Wm,Hm)
			rows,cols = img.shape
			mask = np.zeros(img.shape,np.uint8)
			mask[rows/2-6:rows/2+6,cols/2-6:cols/2+6] = 1
			f = np.fft.fft2(img)
			fshift = np.fft.fftshift(f)
			fshift = fshift*mask
			f2shift = np.fft.ifftshift(fshift)
			img_new = np.fft.ifft2(f2shift)
			s1 = np.abs(img_new)
			return numpy.ndarray.flatten(s1).reshape(Wm,Hm)
		elif(cnt == '3'):
			img = image.reshape(Wm,Hm)
			rows,cols = img.shape
			mask1 = np.ones(img.shape,np.uint8)
			mask1[rows/2-2:rows/2+2,cols/2-2:cols/2+2] = 0
			mask2 = np.zeros(img.shape,np.uint8)
			mask2[rows/2-10:rows/2+10,cols/2-10:cols/2+10] = 1 
			mask = mask1 * mask2
			f = np.fft.fft2(img)
			fshift = np.fft.fftshift(f)
			fshift = fshift*mask
			f2shift = np.fft.ifftshift(fshift)
			img_new = np.fft.ifft2(f2shift)
			s1 = np.abs(img_new)
			return numpy.ndarray.flatten(s1).reshape(Wm,Hm)
if __name__ == '__main__':
	pyimage = Pybh()
	print('ddd')
