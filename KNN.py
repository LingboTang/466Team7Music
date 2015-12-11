from scipy.io import arff
import numpy as np
import operator
import scipy
import sys
import getopt
import os
import math

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for i in range(len(trainingSet)):
        distance = 0
        for j in range(len(testInstance)):
            distance += (testInstance[j]-trainingSet[i][j])**2
        dist = distance
        distances.append((trainingSet[i], dist))
    distances.sort()
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors


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
        data, meta =  arff.loadarff(inputfile)
    except IOError:
        print("Can not find the inputfile!")

    try:
        while os.path.isfile(outputfile):
            os.remove(outputfile)
        ofile = open(outputfile,'w')
    except IOError:
        print("Can not find the outputfile")    
    
    metas = meta.names()
    data_size = len(metas)
    data_array = []
    for datas in data:
        pure_data = list(datas.tolist())
        pure_data.pop()
        data_array.append(pure_data)

    sample_size = len(data_array)

    k = 11
    for i in range(sample_size):
        neighbors = getNeighbors(data_array, data_array[i], k)

    for i in range(11):
        ofile.write(str(neighbors[i]))
        ofile.write("\n")
    ofile.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])