import csv
import re
file=file("train2.csv")
file.readline()
def readTraj():	

	for i in file:
		print i
		result=re.findall(r'-*\d+\.\d+', i)
		print result[1]	
		print len(result)
		n=[]
		for x in range(len(result)/2):
			print x
			n.append([float(result[x*2]),float(result[2*x+1])])	
		file.close()
		return n
if __name__ == '__main__':
	b=readTraj()


