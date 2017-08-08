import csv
import json
import datetime

with open("data/geoCoordinates.tsv") as geoFile:
    geoReader = csv.reader(geoFile, delimiter="\t")
    with open("data/queries_all.json", "w") as allJsonFile, \
            open("data/queries_bots.json", "w") as botJsonFile, \
            open("data/queries_user.json", "w") as userJsonFile, \
            open("data/queries_unknown.json", "w") as unknownJsonFile:
        allData = {}
        botData = {}
        userData = {}
        unknownData = {}
        for i in range(0, 32):
            allData[i] = []
            botData[i] = []
            userData[i] = []
            unknownData[i] = []

        for geoEntry in geoReader:
            month = int(datetime.datetime.strptime(
                geoEntry[3],
                "%Y-%m-%d-%H").strftime("%d"))

            dataPoint = [
                float(geoEntry[0]),
                float(geoEntry[1]),
                1
            ]

            allData[month].append(dataPoint)
            if geoEntry[2] == "UNKNOWN":
                unknownData[month].append(dataPoint)
            elif geoEntry[2] == "USER":
                userData[month].append(dataPoint)
            else:
                botData[month].append(dataPoint)

        json.dump([allData], allJsonFile)
        json.dump([botData], botJsonFile)
        json.dump([userData], userJsonFile)
        json.dump([unknownData], unknownJsonFile)
