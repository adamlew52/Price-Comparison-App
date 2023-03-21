def importHTMLLine(line):
    split = line.split()

    lineList = list(line)
    char = "$"
    char2 = "<"
    trainingData = ""
    #print(lineList)
    #print(lineList.index(char))

    if char in line:
        if char2 in split[0]:
            trainingData = split[0]
            print(f"Code we are looking for: {split[0]}")
        else:
            pass
    else:
        pass

    trainingData = trainingData.replace("<", "")
    trainingData += ", "
    return trainingData

def WriteTrainingData(fileName ,data):
    f = open(fileName, "a")
    f.write(data)
    f.close()

def ElementFrequency(fileName):
    elementData = 0
    WriteTrainingData(fileName, elementData)
    f = open(fileName, "r")
    lines = f.readlines()

    # create a function that scans the file for words in between each comma. 
    # if it has already been counted, enumerate the counter, if not, create a new counter for that value
    # ... essentially tracking the frequency of the data being put in (i.e. how often <span> elements contain our data vs. div elements)


def SkiTest():
    testLine = "<span class=\"money price__current--max\" data-price-max="">$ 449.00</span>|"
    skiTest = importHTMLLine(testLine)
    WriteTrainingData("htmlElementTraining.txt", skiTest)
    ElementFrequency("htmlElementFrequency.txt")

SkiTest()