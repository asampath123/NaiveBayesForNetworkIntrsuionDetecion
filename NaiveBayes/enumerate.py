def enumerateStringColumns(secondColumn, thirdColumn, fourthColumn, classColumn, trainData):
    enum1Count = 1.0
    enum2Count = 1.0
    enum3Count = 1.0
    enumClassCount = 1.0
    for train in trainData:
        # print "....."
        if train[1] not in secondColumn.keys():
            secondColumn[train[1]] = enum1Count
            enum1Count += 1
        if train[2] not in thirdColumn.keys():
            thirdColumn[train[2]] = enum2Count
            enum2Count += 1
        if train[3] not in fourthColumn.keys():
            fourthColumn[train[3]] = enum3Count
            enum3Count += 1
        if train[41] not in classColumn.keys():
            classColumn[train[41]] = enumClassCount
            enumClassCount += 1

    return secondColumn, thirdColumn, fourthColumn, classColumn,enumClassCount,enum1Count,enum2Count,enum3Count


def replaceWithEnumeratedValues(column2, column3, column4, classColumn, trainData):
    for train in trainData:
        train[1] = column2[train[1]]
        train[2] = column3[train[2]]
        train[3] = column4[train[3]]
        #print "Class is",train[41]
        train[41] = classColumn[train[41]]
    return trainData


def replaceWithEnumeratedValuesTest(column2,column3,column4,classTestColumn,trainData,enumClassCount,enum1Count,enum2Count,enum3Count):
    for train in trainData:

        if train[1] not in column2.keys():
            column2[train[1]] = enum1Count
            train[1] = column2[train[1]]
            enum1Count += 1
        else:
            train[1] = column2[train[1]]

        if train[2] not in column3.keys():
            column3[train[2]] = enum2Count
            train[2] = column3[train[2]]
            enum2Count += 1
        else:
            train[2] = column3[train[2]]

        if train[3] not in column4.keys():
            column4[train[3]] = enum3Count
            train[3] = column4[train[3]]
            enum3Count += 1
        else:
            train[3] = column4[train[3]]

        if train[41] not in classTestColumn.keys():
            classTestColumn[train[41]] = enumClassCount
            train[41] = classTestColumn[train[41]]
            enumClassCount += 1
        else:
            train[41] = classTestColumn[train[41]]
    return trainData
