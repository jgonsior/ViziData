import csv
import json
import datetime

with open("data/geoCoordinates.tsv") as geoFile:
    geoReader = csv.reader(geoFile, delimiter="\t")
    with open("data/queries_bots.json", "w") as jsonFile:
        data = {}
        for i in range(0, 32):
            data[i] = []
        i = 0
        for geoEntry in geoReader:
           # if i > 1000:
           #     continue
            month = int(datetime.datetime.strptime(
                geoEntry[3],
                "%Y-%m-%d-%H").strftime("%d"))

            data[month].append([
                float(geoEntry[0]),
                float(geoEntry[1]),
                1
            ])
            i += 1
        json.dump([data], jsonFile)
