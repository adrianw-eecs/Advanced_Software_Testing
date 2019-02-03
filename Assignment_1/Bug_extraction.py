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
medianVal = 0;
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
            # if "<resolution id=" in contents:
            # re.search(r'',contents)
            totalBugCount = totalBugCount + 1
            bugResolution = re.findall('<resolution\sid=\".*\">(.*)</resolution>', contents)
            createdTimeRE = re.findall('<created>(.*)</created>', contents)
            resolutionTimeRE = re.findall('<resolved>(.*)</resolved>', contents)



            # print(value)
            # print("Bug and value is: " + key)
            try:
                if "&apos;" in bugResolution[0]:
                    key = bugResolution[0].replace("&apos;", "'")
                else:
                    key = bugResolution[0]

                if key in resolutionDict:
                    resolutionDict[key] += 1
                    # print("incremented")
                else:
                    resolutionDict[key] = 1
                    # print("created")
                if key == 'Fixed':
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

# for x in resolutionTime:
#     print(x.days)



            # print(value[0])









    # for file in files:
    #     print(file[1])
        # for thefile in file:
            # with open(file) as openFile:
            #
            #     for line in openFile:
            #         potentialBug = False
            #         potentialValue = 99
            #         if "https://issues.apache.org/jira/images/icons/issuetypes/bug.png" in line:
            #             print("Bug matched: " + line)
            #             potentialBug = True
            #         if "<resolution id=" in line:
            #             print("Res matched: " + line)
            #             potentialValue = re.findall('"([^"]*)"', line)
            #         if potentialBug == True and not potentialValue == 99:
            #             print("boug find with value" + potentialValue)








