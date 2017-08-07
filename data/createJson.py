import csv
import json

with open("data/geoCoordinates.tsv") as geoFile:
    geoReader = csv.reader(geoFile, delimiter="\t")
    with open("data/queries_bots.json", "w") as jsonFile:
        data = []
        data.append({2011: []})
        for geoEntry in geoReader:
            geoEntry[0] = float(geoEntry[0])
            geoEntry[1] = float(geoEntry[1])
            geoEntry.append(0)
            data[0][2011].append(geoEntry)

        json.dump(data, jsonFile)
