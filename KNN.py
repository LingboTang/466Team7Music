from scipy.io import arff
import numpy as np
import operator
import scipy
import sys
import getopt
import os
import math


def getNeighbors(trainingData, testTemp, k):
    distances = []
    length = len(testTemp) - 1
    for i in range(len(trainingData)):
        distance = 0
        for j in range(len(testTemp)):
            distance += (testTemp[j]-trainingData[i][j])**2
        dist = distance
        distances.append((trainingData[i], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1))
        return sortedVotes[0][0]

def getAccuracy(testData, predictions):
    correct = 0
    for x in range(len(testData)):
        if testData[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testData))) * 100

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

    train_array = data_array[:len(data_array)//2]
    test_array = data_array[len(data_array)//2+1:]

    sample_size = len(test_array)

    predictions = []
    k = 11
    for i in range(sample_size):
        neighbors = getNeighbors(train_array, test_array[i], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(test_array[i][-1]))

    accuracy = getAccuracy(test_array, predictions)
    ofile.close()
    
if __name__ == "__main__":
    main(sys.argv[1:])