import csv
imagefile=file('image.csv','wb')
py_imagefile=file('py_image.csv','wb')
imagewriter = csv.writer(imagefile)
py_imagewriter = csv.writer(py_imagefile)

def writeImage(image):
	imagewriter.writerow([image])
	imagefile.close()
	
def writePyImage(py_image):
	py_imagewriter.writerow([py_image])
	py_imagefile.close()
