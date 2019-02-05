import pandas
import csv

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

df = pandas.read_csv('../mergeDataET.csv')
print(list(df))

def getData(listLow, listHigh, PC):
    lowData = df[df['userId'].isin(listLow)]
    highData = df[df['userId'].isin(listHigh)]

    scatterLow = int(lowData["nbScatterplot"].mean()*100)/100
    scatterHigh = int(highData["nbScatterplot"].mean()*100)/100

    explLow = int(lowData["why"].mean()*100)/100
    explHigh = int(highData["why"].mean()*100)/100

    slidersLow = int(lowData["slidersExpl"].mean()*100)/100
    slidersHigh = int(highData["slidersExpl"].mean()*100)/100

    artistLow = int(lowData["nbArtistExpl"].mean()*100)/100
    artistHigh = int(highData["nbArtistExpl"].mean()*100)/100

    totalLow = scatterLow

    return [[PC, "low", scatterLow,  explLow, slidersLow, artistLow],
            [PC, "high", scatterHigh, explHigh, slidersHigh, artistHigh]]





with open('interactions.csv', 'w') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(['PC','Group','scatter', 'expl','slider', 'artist'])
    [r1,r2] = getData(lowNFC, highNFC, "NFC")
    [r3,r4] = getData(lowMS, highMS, "MS")
    [r5,r6] = getData(lowVislit, highVislit, "Vislit")
    [r7,r8] = getData(lowVWM, highVWM, "VWM")
    [r9,r10] = getData(lowLoc, highLoc, "Loc")
    w.writerow(r1)
    w.writerow(r2)
    w.writerow(r3)
    w.writerow(r4)
    w.writerow(r5)
    w.writerow(r6)
    w.writerow(r7)
    w.writerow(r8)
    w.writerow(r9)
    w.writerow(r10)


