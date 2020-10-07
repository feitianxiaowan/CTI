import json
import networkx as nx


CONTRLFLOW_EVENT_LIST = ("EVENT_EXECUTE", "EVENT_LOADLIBRARY", "EVENT_CLONE", "EVENT_FORK")
FORWARD_EVENT_LIST = ("EVENT_OPEN", "EVENT_SENDMSG", "EVENT_WRITE", "EVENT_EXECUTE", "EVENT_CLONE", "EVENT_FORK")
RESERVE_EVENT_LIST = ("EVENT_RECVMSG", "EVENT_READ", "EVENT_LOADLIBRARY") # "EVENT_OPEN"?
IGNORE_EVENT_LIST = ("EVENT_CLOSE")

class VertexCentricRDB(object):
    '''
    The Vertex-centric Database is build on Python library "NetworkX"
    '''

    PG = nx.MultiDiGraph()

    eventCount = 1

    def ReadFromDarpaE5Trace(self, logfilePath="/home/zhenyuan/CTI/ta1-trace-1-e5-official-1.bin.1.json"):
        with open(logfilePath) as logfile:

            jsonlogs = logfile.readline()
            while jsonlogs:
                logs = json.loads(jsonlogs)
                datumType = list(logs['datum'].keys())[0]

                if "Event" in datumType:
                    values = logs['datum']['com.bbn.tc.schema.avro.cdm20.Event']
                    eventType = values['type']
                    subjectUuid = values['subject']['com.bbn.tc.schema.avro.cdm20.UUID']
                    objectUuid = values['predicateObject']['com.bbn.tc.schema.avro.cdm20.UUID']

                    if eventType in RESERVE_EVENT_LIST:
                        self.PG.add_edge(objectUuid, subjectUuid, type=eventType, length=0xF)
                    elif eventType in FORWARD_EVENT_LIST:
                        self.PG.add_edge(subjectUuid, objectUuid, type=eventType, length=0xF)
                    elif eventType in IGNORE_EVENT_LIST:
                        pass

                elif "Subject" in datumType:
                    values = logs['datum']['com.bbn.tc.schema.avro.cdm20.Subject']

                    type = "Subject"
                    uuid = values['uuid']
                    eid = values['cid']
                    name = values['properties']['map']['name']

                    self.PG.add_node(uuid, type=type, eid=eid, name=name)

                elif "FileObject" in datumType:
                    values = logs['datum']['com.bbn.tc.schema.avro.cdm20.FileObject']

                    type = "File"
                    uuid = values['uuid']
                    name = values['baseObject']['properties']['map']['path']

                    self.PG.add_node(uuid, type=type, eid=0, name=name)

                elif "NetFlowObject" in datumType:

                    values = logs['datum']['com.bbn.tc.schema.avro.cdm20.NetFlowObject']

                    type = "NetFlow"
                    uuid = values['uuid']
                    remoteAddress = values['remoteAddress']['string']
                    name = values['remoteAddress']['string']

                    self.PG.add_node(uuid, type=type, eid=remoteAddress, name=name)
                else:
                    pass

                jsonlogs = logfile.readline()
                self.eventCount += 1
                if self.eventCount%10000 == 0:
                    print("Event Count: " + str(self.eventCount))

        pass

