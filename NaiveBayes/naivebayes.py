from __future__ import division
import csv
import math
import random
from collections import Counter
from category import *
from enumerate import *
from dataextraction import *
from ClassesandValues import *
from CalculateProbability import *

def accuracyFuntion(testData, allPredictions):
    normalList=[]
    TP=0
    FN=0
    FP=0
    TN=0

    for eachClass in range(len(testData)):
        if float(testData[eachClass][-1]) == allPredictions[eachClass]:
            TP += 1
            TN += 1
        else:
            actual=getkeyFromValue(classColumn, float(testData[eachClass][-1]))
            predicted=getkeyFromValue(classColumn, allPredictions[eachClass])
            if category[actual]== category[predicted]:
                TP += 1
                TN += 1
            else:
                FN += 1
                FP += 1

    for i in range(0,5):
        for eachClass in range(len(testData)):
            if category[getkeyFromValue(classColumn, float(testData[eachClass][-1]))]==i:
                normalList.append(category[getkeyFromValue(classColumn, allPredictions[eachClass])])
                count=normalList.count(i)
        c = Counter(normalList)
        print "consuion matrix values for ",i, "category are ",c.items()
        print "accuracy for ",i, "category is ",round((count/len(normalList))*100.0,2)
        normalList=[]
        count =0



    print "Naive Bayes Classifier , Accuracy value  is %.2f" % round((TP/float(len(testData))) * 100.0,2)

    print "total records", len(testData)
    print "Correctly classified -->",TP
    print "misclassified --------->",FN

    TrueRate = TP / (TP + FN)
    FalseRate = FP / (FP + TN)

    print "True Positive Rate " + str(TrueRate)
    print "FPR Positive Rate " + str(FalseRate)


def getkeyFromValue(dictionary,value):
    for k,v in dictionary.items():
        if v==value:
            return k

if __name__ == "__main__":
    train_fileName = "kddcup.data_10_percent_corrected"
    #train_fileName = "kddcup.data.corrected"
    #filename = "kddcup.testdata.unlabeled_10_percent"
    test_filename = "corrected_test_withLabel"
    #test_filename="testSample"
    trainDataFromFile = []
    testDataFromFile = []
    secondColumn={}
    thirdColumn={}
    fourthColumn={}
    classColumn={}
    category = {}
    trainDataFromFile=extractData(train_fileName)
    testDataFromFile=extractData(test_filename)
    print "done reading train and test"





    secondColumn,thirdColumn,fourthColumn,classColumn,enumClassCount,enum1Count,enum2Count,enum3Count=enumerateStringColumns(secondColumn,thirdColumn,fourthColumn,classColumn,trainDataFromFile)
    trainDataFromFile = replaceWithEnumeratedValues(secondColumn, thirdColumn, fourthColumn,classColumn, trainDataFromFile)
    testDataFromFile = replaceWithEnumeratedValuesTest(secondColumn, thirdColumn, fourthColumn,classColumn, testDataFromFile,enumClassCount,enum1Count,enum2Count,enum3Count)
    print "classColumn", classColumn
    category=groupClasses(classColumn)
    print "categorise classes"
    classeswithRecords = MapofClassWithItsRecords(trainDataFromFile)
    print "got all class records"
    allPredictions = getAllPredictions(classeswithRecords, testDataFromFile)
    print "got all predictions"
    #print "allPredictions",allPredictions
    accuracyFuntion(testDataFromFile, allPredictions)
