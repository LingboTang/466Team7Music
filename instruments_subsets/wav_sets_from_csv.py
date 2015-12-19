import shutil
import sys
import os

subsetname = "V_and_C_only"	# change this value to D_only, D_and_C_only, etc.. as specified in the csv_subsets directory

inputf = "csv_subsets/subset_"+ subsetname + ".csv"

try:
	subset = open(inputf, 'r')
except:
	print('Something went wrong! Can\'t tell what?')
	sys.exit(0) # quit Python

data = subset.readlines()

inputdir = "/Users/Maxime/Documents/University/2015/Cmput466/Project/ILAM_samples_wav/"
outputdir = "wav_subsets/"+subsetname#+'/'

if not os.path.exists(outputdir):
    os.makedirs(outputdir)  

for line in data:
	track = line.split(';')[0]
	title = track + ".wav"
	srcfile = inputdir + title
	dstfile = outputdir + title 
	shutil.copy2(srcfile, outputdir)