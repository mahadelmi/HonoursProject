import numpy as np
import os
#filename = "/Users/mahadelmi/Documents/HonoursProject/usneedle_data/NoviceData/1_B-20170602-102042/NeedleTipToImage-Sequence.mha"
folderName = "/Users/mahadelmi/Documents/HonoursProject/usneedle_data/NoviceData"
transformTypes = ["ImageToReference", "NeedleTipToImage", "NeedleToReference", "ImageToReference", "NeedleToProbe", "ProbeToReference","NeedleTipToReference"]
#translationsTypes = ["Translation", "Quaternion", "AxisAngle", "Euler","Matrix6D","RotationMatrix""]
def readfile(fileName):
    #print(fileName)
    with open(fileName, "r") as f:

        transforms = []
        totalRotations = []
        totalTranslations = []
        slices = []

        for line in f:
            #line = line.replace("="," ")

            transformStatus = ""
            transformStats = []
            line = line.replace("="," ")
            splitLine = line.split("\n")[0].split(" ")
            #print(splitLine)
            #ignore matrix at the end. Positions that are rotations are 1-3, 5-7, 9-11 and the positions for translations are 4,8,12
            currRotations = []
            currTranslations = []
            for transformType in transformTypes:
                #print(splitLine[0])
                if(transformType in splitLine[0] and "Status" not in splitLine[0]):
                    currSlice = list(map(float,splitLine[2:14]))
                    #print(currSlice)
                    slices.append(np.array(currSlice))
                    """
                    for i in range(2,14,4):
                        currSlice =
                        currRotations.append([splitLine[i],splitLine[i+1],splitLine[i+2]])
                        currTranslations.append(splitLine[i+3])
                    totalRotations.append(currRotations)
                    totalTranslations.append(currTranslations)
                    """
                elif("Timestamp" in splitLine[0]):
                    print(splitLine)

        #print(np.array(totalRotations))
        #slices = np.array(slices)
        #print(np.array(slices).shape)
        return slices

#print(readfile(filename))
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
noviceSlices = []
expertSlices = []
for i in range(1,41):
    if(i==23 or i==28):
        continue
    indexedFiles = [filename for filename in os.listdir(folderName) if filename.startswith(str(i) + "_")]
    participantSlices = []

    for filename in indexedFiles:
        if(".sqbr" not in filename):
            if("B" in filename):
                b_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                c1+=1
                print("B: " + str(b_slices.shape))
            elif("T1" in filename):
                t1_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                c2+=1
                print("T1: " + str(t1_slices.shape))
            elif("T2" in filename):
                t2_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                c3+=1
                print("T2: " + str(t2_slices.shape))
            elif("T3" in filename):
                t3_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                print("T3: " + str(t3_slices.shape))
                c4+=1
            elif("T4" in filename):
                t4_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                print("T4: " + str(t4_slices.shape))
                c5+=1
            elif("F" in filename):
                f_slices = readfile(folderName + "/" + filename + "/ImageToReference-Sequence.mha")
                print("F: " + str(f_slices.shape))
                c6+=1
    participantSlices = [b_slices, t1_slices, t2_slices, t3_slices, f_slices]
    noviceSlices.append(participantSlices)
print(noviceSlices)

"""
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
"""
