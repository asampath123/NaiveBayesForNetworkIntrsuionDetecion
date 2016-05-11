def extractData(fileName):
    DataFromFile=[]
    file = open(fileName, 'r')
    for everyLine in file:
        values = everyLine.strip().split(",")
        DataFromFile.append(values)
    file.close()

    for i in range(len(DataFromFile)):
        for j in range(len(DataFromFile[i])):
            if DataFromFile[i][j].isdigit():
                DataFromFile[i][j] = float(DataFromFile[i][j])+1
            elif isFloat(DataFromFile[i][j]):
                DataFromFile[i][j] = float(DataFromFile[i][j])+1
            else:
                DataFromFile[i][j] = DataFromFile[i][j]

    return DataFromFile


def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False