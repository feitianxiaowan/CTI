import json


class DarpaE5TraceParser(object):
    def __init__(self):
        pass

    def DatumTypeCount(self, logfilePath="/home/zhenyuan/CTI/ta1-trace-1-e5-official-1.bin.1.json"):
        """ Count the occurrence of each type of datum in one.

        :arg:
            Path of logfile.

        :return:
            {'com.bbn.tc.schema.avro.cdm20.Event':        3,787,514,
             'com.bbn.tc.schema.avro.cdm20.MemoryObject':   648,856,
             'com.bbn.tc.schema.avro.cdm20.Subject':        112,912,
             'com.bbn.tc.schema.avro.cdm20.SrcSinkObject':  307,958,
             'com.bbn.tc.schema.avro.cdm20.IpcObject':       23,240,
             'com.bbn.tc.schema.avro.cdm20.NetFlowObject':   15,283,
             'com.bbn.tc.schema.avro.cdm20.FileObject':      17,582,
             'com.bbn.tc.schema.avro.cdm20.UnitDependency':  86,655}
        """
        with open(logfilePath) as logfile:
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

        return datumTypeSet
        pass

    def ExtractFromEvent(self, logs):
        values = logs['datum']['com.bbn.tc.schema.avro.cdm20.Event']

        uuid = values['uuid']
        subjectUuid = values['subject']['com.bbn.tc.schema.avro.cdm20.UUID']
        objectUuid = values['predicateObject']['com.bbn.tc.schema.avro.cdm20.UUID']
        eventType = values['type']

        output = "event," + uuid + "," + subjectUuid + "," + objectUuid + "," + eventType + "\n"
        return output
        pass

    def ExtractFromSubject(self, logs):
        values = logs['datum']['com.bbn.tc.schema.avro.cdm20.Subject']

        uuid = values['uuid']
        parentUuid = values['parentSubject']['com.bbn.tc.schema.avro.cdm20.UUID']
        cid = values['cid']
        name = values['properties']['map']['name']
        command = values['cmdLine']['string']

        output = "subject," + uuid + "," + parentUuid + "," + cid + "," + name + "," + command + "\n"
        return output
        pass

    # Default extractor for all objects
    def ExtractFromObject(self, logs):
        values = list(logs['datum'].values())[0]

        uuid = values['uuid']
        objectType = logs['type']

        output = "object," + uuid + "," + objectType + "\n"
        return output
        pass

    # Extractor for other detailed objects
    def ExtractFromFileObject(self, logs):
        values = logs['datum']['com.bbn.tc.schema.avro.cdm20.FileObject']

        uuid = values['uuid']
        path = values['properties']['map']['path']

        output = "fileObject," + uuid + "," + path + "\n"
        return output
        pass

    def ExtractFromFileObject(self, logs):
        values = logs['datum']['com.bbn.tc.schema.avro.cdm20.FileObject']

        uuid = values['uuid']
        path = values['baseObject']['properties']['map']['path']

        output = "fileObject," + uuid + "," + path + "\n"
        return output
        pass

    def ExtractFromNetFlowObject(self, logs):
        values = logs['datum']['com.bbn.tc.schema.avro.cdm20.NetFlowObject']

        uuid = values['uuid']
        remoteAddress = values['remoteAddress']['string']

        output = "netFlowObject," + uuid + "," + remoteAddress + "\n"
        return output
        pass

    def BasicParser(self, logfilePath="/home/zhenyuan/CTI/ta1-trace-1-e5-official-1.bin.1.json",
                    outputfilePath="/home/zhenyuan/CTI/ta1-trace-1-e5-offcial-1.bin.1.json.csv"):
        with open(logfilePath) as logfile, open(outputfilePath, "w+") as outputFile:
            jsonlogs = logfile.readline()

            while jsonlogs:
                logs = json.loads(jsonlogs)
                datumType = list(logs['datum'].keys())[0]

                if "Event" in datumType:
                    outputFile.write(self.ExtractFromEvent(logs))
                elif "FileObject" in datumType:
                    outputFile.write(self.ExtractFromFileObject(logs))
                elif "NetFlowObject" in datumType:
                    outputFile.write(self.ExtractFromNetFlowObject(logs))
                elif "Object" in datumType:
                    outputFile.write(self.ExtractFromObject(logs))
                else:
                    pass

                jsonlogs = logfile.readline()
        pass


if __name__ == '__main__':
    DarpaE5TraceParser().BasicParser()

    pass
