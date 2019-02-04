import os
import glob
from collections import defaultdict
from datetime import datetime
import re
import math

# import xml.etree.ElementTree as ET
totalfileCount = 0
totalfailedCount = 0
totalBugCount = 0
resolutionDict = defaultdict(int)
resolutionTime = []
statusDict = defaultdict(int)
medianVal = 0
issueTypeDict = defaultdict(int)
# for files in os.walk("C:/Users/adria/Documents/4313/Assignment_1/Test"):
# path = "C:/Users/adria/Documents/4313/Assignment_1/Test"
path = "C:/Users/adria/Documents/4313/Assignment_1/hbaseBugReport"
listFiles = os.listdir(path)
# print(listFiles)
for file in listFiles:
    # print("1")
    with open(path + "/" + file) as f:
        # print(file)
        totalfileCount += 1
        contents =f.read()
        # print("2")
        isBug = re.findall('<type\sid=\".*\"\siconUrl=\".*\">(.*)</type>', contents)

        try:

            if isBug[0] in issueTypeDict:
                issueTypeDict[isBug[0]] += 1
                # print("incremented")
            else:
                issueTypeDict[isBug[0]] = 1
        except:
            print("failed")


        if isBug[0] == "Bug":
            totalBugCount = totalBugCount + 1
            bugres2 = re.findall('<status\sid=\".*\"\siconUrl=\".*\"\sdescription=\".*\">(.*)<\/status>', contents)
            bugResolution = re.findall('<resolution\sid=\".*\">(.*)</resolution>', contents)
            createdTimeRE = re.findall('<created>(.*)</created>', contents)
            resolutionTimeRE = re.findall('<resolved>(.*)</resolved>', contents)

            try:
                # print(bugResolution)
                if "&apos;" in bugResolution[0]:
                    key1 = bugResolution[0].replace("&apos;", "'")
                else:
                    key1 = bugResolution[0]

                key2 = bugres2[0]
                if key2 in statusDict:
                    statusDict[key2] += 1
                    # print("incremented")
                else:
                    statusDict[key2] = 1
                    # print("created")

                if key1 in resolutionDict:
                    resolutionDict[key1] += 1
                    # print("incremented")
                else:
                    resolutionDict[key1] = 1
                    # print("created")

                if key2 == 'Closed' or key1 == "Fixed":
                    createDate = datetime.strptime(createdTimeRE[0], "%a, %d %b %Y %H:%M:%S %z")
                    resolutionDate = datetime.strptime(resolutionTimeRE[0], "%a, %d %b %Y %H:%M:%S %z")
                    totalTime = resolutionDate - createDate
                    totalTime = totalTime.days
                    resolutionTime.append(totalTime)
            except:
                totalfailedCount += 1
                print(file)
                # print("FAILED MISSERABLY")


print("Total amount of Bug Reports: ", str(totalfileCount))
print("Total Falied to process: ", str(totalfailedCount))
print(dict(issueTypeDict))
print("Total Amount of bugs: ", str(totalBugCount))
print(dict(statusDict))
print(dict(resolutionDict))

print("---------------------------------------------------------------------")
print("Fixed Bugs, resolution times below")
# print(resolutionTime)
resolutionTime.sort()
print("Average resolution time:", sum(resolutionTime)/float(len(resolutionTime)))
print("Minimum resolution time:", resolutionTime[0])
print("Maximum resolution time:", resolutionTime[len(resolutionTime)-1])
if (len(resolutionTime)-1) % 2 == 0:
    medianVal = resolutionTime[int((len(resolutionTime) - 1) / 2)]
else:
    medianVal = resolutionTime[math.ceil((len(resolutionTime) - 1) / 2)]
    medianVal = medianVal + resolutionTime[math.ceil((len(resolutionTime) - 1) / 2)]



print("Median resolution time:", medianVal)
