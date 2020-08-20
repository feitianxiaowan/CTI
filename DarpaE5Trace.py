import json

with open("/home/zhenyuan/CTI/ta1-trace-1-e5-official-1.bin.1.json") as logfile:
    jsonlogs = logfile.readline()

    datumTypeSet = set()
    datumTypeCount = dict()
    while jsonlogs:
        logs = json.loads(jsonlogs)
        datumType = list(logs['datum'].keys())[0]

        if datumType not in datumTypeSet:
            print(logs)
            datumTypeCount[datumType] = 0

        datumTypeSet.add(datumType)
        datumTypeCount[datumType] += 1

        jsonlogs = logfile.readline()