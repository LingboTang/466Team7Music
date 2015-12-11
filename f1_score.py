import numpy
import scipy
import os
import sys
import getopt


def main(argv):
	
	inputfile = ''
	outputfile = ''
	prefix = 'Matrix'

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('f1_score.py -i <inputfile> -o <outputfile>')
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print('f1_score.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i","--ifile"):
			inputfile = arg
		elif opt in ("-o","--ofile"):
			outputfile = arg

	try:
		ifile = open(inputfile,'r')
	except IOError:
		print("Can not find the inputfile!")

	try:
		while os.path.isfile(outputfile):
			outputfile = input("File Exists. Enter name again > ")
		ofile = open(outputfile,'w')
	except IOError:
		print("Can not find the outputfile")

	Matrix_value = []
	for line in ifile:
		line = line.strip('\n')
		if (len(line)!=0):
			Matrix_value.append(line)

	ifile.close()
	ofile.close()

	for strings in Matrix_value:
		if (prefix in strings):
			index = Matrix_value.index(strings)

	KK = Matrix_value[index+2].split(' ')
	PP = Matrix_value[index+3].split(' ')
	TP = []
	TN = []
	FP = []
	FN = []

	i = 0
	counter = 0
	while counter < 2:
		if((KK[i] != '') and (counter == 0)):
			TN.append(int(KK[i]))
			counter +=1
		elif((KK[i] != '') and (counter == 1)):
			FP.append(int(KK[i]))
			counter +=1
		i +=1

	i = 0
	counter = 0
	while counter < 2:
		if((PP[i] != '') and (counter == 0)):
			FN.append(int(PP[i]))
			counter +=1
		elif((PP[i] != '') and (counter == 1)):
			TP.append(int(PP[i]))
			counter +=1
		i+=1

	try:
		f1_score = 2*sum(TP)/(2*sum(TP)+ sum(FP) + sum(FN))
		print(f1_score)
	except ZeroDivisionError :
		print("No Data")

	
if __name__ == "__main__":
   main(sys.argv[1:])