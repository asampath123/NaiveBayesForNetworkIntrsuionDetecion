import math
def probabilityCalculator(attr, mean, stdDev):
    tempVal=(-(math.pow(attr - mean, 2) / (2 * math.pow(stdDev, 2))))
    exponentVal = math.exp(tempVal)
    returnProb=(1 / (math.sqrt(2*math.pi) * stdDev)) * exponentVal
    return returnProb

def eachClassProbablilty(classesWithRecordsData, record):
    probabilityDict = {}
    for classes, eachRecord in classesWithRecordsData.iteritems():
        probabilityDict[classes] = 1
        for item in range(len(eachRecord)):
            avg, stdDev = eachRecord[item]
            attribute = record[item]
            probabilityDict[classes] *= probabilityCalculator(float(attribute), avg, stdDev)
    return probabilityDict

def mainPrediction(classesWithRecordsData, record):
    probabilityDict = eachClassProbablilty(classesWithRecordsData, record)
    #print "probabilities",probabilities
    classLabel = "noneFound"
    classProb = -1
    for classes, prob in probabilityDict.iteritems():
        if classLabel is "noneFound" or prob > classProb:
            classProb = prob
            classLabel = classes
    return classLabel

def getAllPredictions(classesWithRecordsData, testData):
    predicitonionForallClasses = []
    for eachRecord in range(len(testData)):
        predicitonionForEachRecord = mainPrediction(classesWithRecordsData, testData[eachRecord])
        predicitonionForallClasses.append(predicitonionForEachRecord)
    return predicitonionForallClasses