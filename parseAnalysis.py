from os import listdir
import csv
import heatmap
import transitions

q1NFC = [3,10,13,14,16,25,29,30]
q2NFC = [5,12,22,23,26,27,28]
q3NFC = [2,4,7,9,18,19,24]
q4NFC = [1,6,8,11,15,17,20,21]
test = [29]

lowNFC = [3,10,13,14,16,25,29,30,5,12,22,23,26,27,28]
highNFC = [2,4,7,9,18,19,24, 1,6,8,11,15,17,20,21 ]

lowVislit = [1,2,3,4,5,6,7,8,9,11,13,14,17,19,20,23,25,26,28,29,30]
highVislit = [10,12,15,16,18,21,22,24,27]

lowMS = [2,5,7,8,10,11,12,13,14,16,19,20,21,23,29,30]
highMS = [1,3,4,6,9,15,17,18,22,24,25,26,27,28]

lowLoc = [2,4,5,9,11,12,15,16,17,18,19,21,22,26,30]
highLoc = [1,3,6,7,8,10,13,14,20,23,24,25,27,28,29] #hoge interne locus of control;

lowVWM = [2,3,4,5,6,7,8,9,10,12,13,14,15,17,20,22,23,24,25,26,27,28,30]
highVWM = [1,11,16,18,19,21,29]

# analyse file
def parseFile(file):
    with open(file) as f:
        content = f.readlines()
        content = [parseLine(x) for x in content]
        dict1 = createHeatmapData(content)
        dict2 = createTransitionsData(content)
        result = {**dict1, **dict2}
        return result

def parseLine(line):
    splitted = line.split('\t')
    return (int(splitted[1]) / 1000 , splitted[2].strip())

def createHeatmapData(content):
    '''
    Create percentage of time user spent at each AOI
    :param content:
    :return:
    '''
    dictValues = {"start": 0, "a": 0, "r": 0, "s": 0, "e": 0, "w": 0, "d": 0}
    totalTime = 0
    for i in range(0, len(content) - 2):
        current = content[i]
        timeCurrent = current[0]
        elementCurrent = current[1]
        if elementCurrent != "?":
            timeNext = content[i + 1][0]
            timeRange = int(timeNext) - int(timeCurrent)
            dictValues[elementCurrent] += timeRange
            totalTime += timeRange

    for key in dictValues.keys():
        dictValues[key] = int(dictValues[key] * 100 / totalTime )
    return dictValues

def createTransitionsData(content):
    '''
    Calculate the different transitions
    :param content:
    :return:
    '''
    dictValues = {"start_a": 0, "start_r": 0, "start_s": 0, "start_e":0, "start_w":0, "start_d": 0,
                  "a_r": 0, "a_s": 0, "a_e": 0, "a_w": 0, "a_d": 0,
                  "r_s": 0, "r_e": 0, "r_w": 0, "r_d": 0,
                  "s_e":0, "s_w":0, "s_d": 0,
                  "e_w":0, "e_d": 0,
                  "w_d":0
    }
    for i in range(0, len(content) - 2):
        current = content[i][1]
        next = content[i + 1][1]
        if next == "?":
            next = content[i + 2][1]

        if current != next and current != "?":
            key1 = current + "_" + next
            key2 = next + "_" + current
            if key1 in dictValues:
                dictValues[key1] += 1
            else:
                dictValues[key2] += 1
    return dictValues

def parseFileName(file, participants, index):
    splitted = file.split('-')
    p = splitted[0].strip()
    interface = splitted[1].strip()
    if (p not in participants):
        participants[p] = index
        index += 1

    participant = participants[p]
    expl = False if interface == "base" else True
    return [participant, expl, participants, index]

def addDictionaries(dict1, dict2):
    if dict1 == {}:
        return dict2
    else:
        totalDict = {}
        for key in dict2:
            totalDict[key] = dict1[key] + dict2[key]
        return totalDict

def mainVisualise(list, name):
    with open('mycsvfile.csv', 'w') as f:
        # list all files
        mypath = './analysis'
        participants = {}
        index = 0
        nbA = 0
        nbR = 0
        nbW = 0
        nbD = 0
        nbS = 0
        nbE = 0
        totalDict = {}
        for file in listdir(mypath):
            dict = parseFile(mypath + "/" + file)
            [participant, expl, participants, index] = parseFileName(file, participants, index)
            dictRow = {'p': participant, 'expl': expl, **dict}
            if index == 1:
                w = csv.DictWriter(f, dictRow.keys())
                w.writeheader()

            # write to csv
            w.writerow(dictRow)

            if dictRow['expl']  and dictRow['p'] in list:
                # add percentages
                nbA += dict['a'] / 100.0
                nbR += dict['r'] / 100.0
                nbW += dict['w'] / 100.0
                nbD += dict['d'] / 100.0
                nbS += dict['s'] / 100.0
                nbE += dict['e'] / 100.0
                totalDict = addDictionaries(totalDict, dictRow)

        nbInList = len(list)
        # normalise numbers and generate heatmap of average percentage of time user spent in AOI
        matrix = heatmap.generateMatrixExpl(nbA/nbInList, 0, nbW/nbInList, nbD/nbInList, nbS/nbInList, nbE/nbInList)
        heatmap.createHeatmapExpl(matrix, 'heatmap/'+ name + '.png')
        # average (absolute) number of transistions between AOI
        normalisedDict = {k: round(v / nbInList) for k, v in totalDict.items()}
        # transitions.displayTransitionsExpl(normalisedDict, 'transitions/'+ name + '.png')


if __name__ == '__main__':
    listLists = [lowNFC, highNFC, lowMS, highMS, lowLoc, highLoc, lowVWM, highVWM, lowVislit, highVislit]
    listName = ['lowNFC', 'highNFC', 'lowMS', 'highMS', 'lowLoc', 'highLoc', 'lowVWM', 'highVWM', 'lowVislit', 'highVislit']

    for i in range(0,len(listLists)):
        listDV = listLists[i]
        name = listName[i]
        mainVisualise(listDV, name)



