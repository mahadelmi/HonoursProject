from datetime import datetime, timedelta
import csv
import numpy as np
import os
path = "/Users/mahadelmi/Documents/HonoursProject/usneedle_data/"
transformTypes = ["ImageToReference", "NeedleTipToImage", "NeedleToReference", "ImageToReference", "NeedleToProbe", "ProbeToReference","NeedleTipToReference"]
transformFiles = ["ImageToReference-Sequence.mha", "NeedleTipToImage-Sequence.mha","NeedleToReference-Sequence.seq.mha","ImageToReference-Sequence.mha",
"NeedleToProbe-Sequence.seq.mha","ProbeToReference-Sequence.seq.mha","NeedleTipToReference-Sequence.mha"]
noviceStuff = []
arbitraryDate = datetime(2019,10,27)
expertSize = 5
noviceSize = 40
#def findNumFrames(fileName):
transformFile = transformFiles[0]
def findNumFrames(fileName):
    numFrames = 0
    with open(fileName, "r") as f:
        for line in f:
            line = line.replace("="," ")
            splitLine = line.split("\n")[0].split(" ")
            if("Timestamp" in splitLine[0]):
                numFrames+=1
                #timeIncrements+=int(1000*float(splitLine[3]))
    return numFrames

def fillInVals(dateTimes,slices, avgTime, maxFrames):
    #initTime =
    #print(avgTime)
    for i in range(len(dateTimes),maxFrames):
        #print("hi")
        newTime = dateTimes[i-1] + timedelta(milliseconds = 1000*avgTime)
        dateTimes.append(newTime)
        slices.append([0,0,0,0,0,0,0,0,0,0,0,0])
    #print(np.array(slices).shape)
    return [dateTimes, slices]

def readfile(fileName):
    #print(fileName)
    #biggestTime = 0
    with open(fileName, "r") as f:
        dateTimes = []
        c1=0
        c2=0
        transforms = []
        totalRotations = []
        totalTranslations = []
        slices = []
        file = fileName.split("/")[-2].split("-")
        biggestTime = 0
        #print(file)
        #print(file[1] + file[2])
        #initTime = datetime.strptime(file[1] + file[2], "%Y%m%d%H%M%S")
        initTime = arbitraryDate
        for type in transformTypes:
            if(type in fileName):
                transformType = type
        for line in f:
            #line = line.replace("="," ")

            transformStatus = ""
            transformStats = []
            line = line.replace("="," ")
            splitLine = line.split("\n")[0].split(" ")
            #ignore matrix at the end. Positions that are rotations are 1-3, 5-7, 9-11 and the positions for translations are 4,8,12
            currRotations = []
            currTranslations = []
            if("Timestamp" in splitLine[0]):
                frameTime  = initTime + timedelta(milliseconds = 1000*float(splitLine[3]))
                dateTimes.append(frameTime)
                if(biggestTime<float(splitLine[3])):
                    biggestTime =float(splitLine[3])
                #sumTimes += int(float(splitLine[3]))
            elif(transformType in splitLine[0] and "Status" not in splitLine[0]):
                currSlice = list(map(float,splitLine[2:14]))
                #slices.append(np.array(currSlice))
                slices.append(currSlice)


        #slices = np.array(slices)
        #print(str(biggestTime) + "," + str(biggestTime/len(dateTimes)))

        return [dateTimes,slices, biggestTime/len(dateTimes)]

maxFrames = 0
for i in range(1,noviceSize+1):
    fullPath = path + "NoviceData"
    if(i==23 or i==28):
        continue
    indexedFiles = [filename for filename in os.listdir(fullPath) if filename.startswith(str(i) + "_")]
    for filename in indexedFiles:
        if(".sqbr" not in filename):
            numFrames = findNumFrames(fullPath + "/" + filename + "/" + transformFile)
            #print(maxFrames)
            if(numFrames>maxFrames):
                #print(filename)
                maxFrames=numFrames
for i in range(1,expertSize+1):
    fullPath = path + "ExpertData"
    indexedFiles = [filename for filename in os.listdir(fullPath) if filename.startswith(str(i) + "_")]
    for filename in indexedFiles:
        if(".sqbr" not in filename):
            numFrames = findNumFrames(fullPath + "/" + filename + "/" + transformFile)
            if(numFrames>maxFrames):
                #print(filename)
                maxFrames=numFrames
data = []
csvData = []
IPData = []
OOPData = []
#print(maxFrames)

#Novices
skillLevel = "Novice"
skill = 0
#maxFrames = 0

for i in range(1,noviceSize+1):
    fullPath = path + "NoviceData"
    if(i==23 or i==28):
        continue
    indexedFiles = [filename for filename in os.listdir(fullPath) if filename.startswith(str(i) + "_")]
    if(i%2==1):
        method = "IP"
    else:
        method = "OOP"
    participantInfo = []
    for filename in indexedFiles:
        if(".sqbr" not in filename):
            if("B" in filename):
                phase = "B"
                orderNum = 0
            elif("T1" in filename):
                phase = "T1"
                orderNum = 1
            elif("T2" in filename):
                phase = "T2"
                orderNum = 2
            elif("T3" in filename):
                phase = "T3"
                orderNum = 3
            elif("T4" in filename):
                phase = "T4"
                orderNum = 4
            elif("F" in filename):
                phase = "F"
                orderNum = 5
            dateTimes,slices, avgTime = readfile(fullPath + "/" + filename + "/" + transformFile)
            #print(avgTime)
            dateTimes,slices = fillInVals(dateTimes,slices,avgTime,maxFrames)
            #print(np.array(slices).shape)
            participantInfo.append([orderNum,phase,dateTimes,slices])

            #print(len(dateTimes))
        #order phases
    #print(len(participantInfo))
    participantInfo.sort(key=lambda phase: phase[0])

    for j in range(len(participantInfo)):
        _,phase,dateTimes,slices = participantInfo[j]
        #print(len(slices))


        for k in range(len(dateTimes)):
            csvLine = [skillLevel, i, phase, dateTimes[k], k, str(slices[k]), skill]
            #print(csvLine)
            if(method=="IP"):
                IPData.append(csvLine)
            else:
                OOPData.append(csvLine)
            csvLine = [skillLevel, i, phase, dateTimes[k], k, str(slices[k]), method, skill]
            csvData.append(csvLine)

#print(len(csvData))




#Experts
skillLevel = "Expert"
skill = 1
for i in range(1,expertSize+1):
    fullPath = path + "ExpertData"
    indexedFiles = [filename for filename in os.listdir(fullPath) if filename.startswith("E" + str(i) + "_")]
    #print(indexedFiles)
    expertInfo = []
    for filename in indexedFiles:
        if(".sqbr" not in filename):
            if("IP" in filename):
                #print("IP:" + filename)
                method = "IP"
            else:
                #print("OOP:" + filename)
                method = "OOP"
            if("P2" in filename):
                version = "2"
            else:
                version = "1"
            #dateTimes,slices, avgTime = readfile(fullPath + "/" + filename + "/" + transformFile)
            dateTimes,slices, avgTime = readfile(fullPath + "/" + filename + "/" + transformFile)
            dateTimes,slices = fillInVals(dateTimes,slices,avgTime,maxFrames)
            #print(filename.split("-")[0].split("_")[1])
            #print(np.array(slices).shape)
            expertInfo.append([filename.split("-")[0].split("_")[1],method, version,dateTimes,slices])
            #print("E"+str(i) + "," + filename.split("-")[0].split("_")[1]+": "+str(len(dateTimes)))
    expertInfo.sort(key=lambda expertMethod: expertMethod[0])
    #print(expertInfo)
    #print("E"+str(i) + "," + filename.split("-")[0].split("_")[1]+": "+str(len(dateTimes)))
    #print(expertInfo)
    for j in range(len(expertInfo)):
        #print("E" + str(i) + "_" + expertInfo[j][0])
        #print("E" + str(i) + "_" + method + str(ve))
        _,method, version,dateTimes,slices = expertInfo[j]
        #print("E" + str(i) + "_" + method + str(version))
        #print("E" + str(i) + "_" + version + ":" + method)
        #print("E"+str(i) + "," + filename.split("-")[0].split("_")[1]+": "+str(len(dateTimes)))
        for k in range(len(dateTimes)):
            csvLine = [skillLevel, i, version, dateTimes[k], k, str(slices[k]), skill]
            #csvLine = [skillLevel, i, "N/A", dateTimes[k], k, method, skill]
            #print(csvLine)
            #print(len(dateTimes))
            if(method=="IP"):
                #print("IP: "+ "E" + str(i) + "_" + expertInfo[j][0])
                IPData.append(csvLine)
            else:
                #print("OOP: "+ "E" + str(i) + "_" + expertInfo[j][0])
                OOPData.append(csvLine)
            csvLine = [skillLevel, i, version, dateTimes[k], k, str(slices[k]), method, skill]
            csvData.append(csvLine)
#print(len(csvData[0]))
print(np.array(OOPData).shape)
print(np.array(IPData).shape)
with open(path +'usneedledata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['Novice/Expert','ID', 'Phase', 'Datetime', 'Frame', 'Matrix', 'Method', 'Skill']
    writer.writerow(header)
    for csvLine in csvData:
        writer.writerow(csvLine)

with open(path + 'OOP/' +'usneedledata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['Novice/Expert','ID', 'Phase', 'Datetime', 'Frame', 'Matrix', 'Skill']
    writer.writerow(header)
    for csvLine in OOPData:
        writer.writerow(csvLine)
with open(path +'IP/'+ 'usneedledata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['Novice/Expert','ID', 'Phase', 'Datetime', 'Frame', 'Matrix', 'Skill']
    writer.writerow(header)
    for csvLine in IPData:
        writer.writerow(csvLine)


noviceNum=1
expertNum = 1
phase = "B"
version = "1"
dataDict = {"IP":{},"OOP":{}}

for i in range(len(csvData)):
    method = csvData[i][6]
    if(csvData[i][0]=="Novice"):
        if(csvData[i][1]!=noviceNum or csvData[i][2]!=phase):
            noviceNum = csvData[i][1]
            phase = csvData[i][2]
        #print("N" + str(noviceNum) +"_"+ phase)
        if("N" + str(noviceNum) +"_" + phase in dataDict[method]):
            dataDict[method]["N" + str(noviceNum) +"_"+ phase].append(csvData[i])
        else:
            dataDict[method]["N" + str(noviceNum) +"_"+ phase] = [csvData[i]]
    else:
        if(csvData[i][1]!=expertNum or csvData[i][2]!=version):
            expertNum = csvData[i][1]
            version = csvData[i][2]
        else:
            if("E" + str(expertNum) +"_"+ version in dataDict[method]):
                dataDict[method]["E" + str(expertNum) +"_"+ version].append(csvData[i])
            else:
                dataDict[method]["E" + str(expertNum) +"_"+ version] = [csvData[i]]
for method in dataDict:
    #print(method + ": " + str(dataDict[method].keys()))
    for key in dataDict[method]:
        with open(path +'allData/' + method + "/"+ key + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            #header = ['Novice/Expert','ID', 'Phase/Version', 'Datetime', 'Frame', 'Matrix', 'Skill']
            header = ['date', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12',  'Skill']
            writer.writerow(header)
            participantData = dataDict[method][key]
            #print(np.array(participantData).shape)
            #print()
            for csvLine in participantData:
                slices = csvLine[5].replace('[','').replace(']','').split(",")
                #print(csvLine[5].replace('[','').replace(']','').split(","))
                if(len(slices)<12):
                    print("Len" + str(len(slices)))
                    print("Slices" + str(slices))

                writer.writerow([csvLine[3], slices[0], slices[1], slices[2],
                  slices[3], slices[4], slices[5],
                   slices[6], slices[7], slices[8],
                    slices[9], slices[10], slices[11], csvLine[7]])
                
