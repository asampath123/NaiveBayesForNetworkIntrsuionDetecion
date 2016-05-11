import math

def identifyClass(trainData):
    tempClassesDict = {}
    for i in range(len(trainData)):
        each_line = trainData[i]
        if (each_line[-1] not in tempClassesDict):
            tempClassesDict[each_line[-1]] = []
        tempClassesDict[each_line[-1]].append(each_line)
    return tempClassesDict

def meanAndStd(trainData):
    summaries = [(sum(data) / float(len(data)), std_dev(data)) for data in zip(*trainData)]
    del summaries[-1]
    return summaries


def MapofClassWithItsRecords(trainData):
    separated = identifyClass(trainData)
    classWithRows = {}
    #print separated
    for classes, rows in separated.iteritems():
        classWithRows[classes] = meanAndStd(rows)
    return classWithRows

def std_dev(number):
    avg = sum(number)/float(len(number))
    x1=sum([pow(num-avg,2) for num in number])
    x2=float(len(number)-1)
    result = x1/x2
    if math.sqrt(result)==0.0:
        return 0.01
    return math.sqrt(result)


