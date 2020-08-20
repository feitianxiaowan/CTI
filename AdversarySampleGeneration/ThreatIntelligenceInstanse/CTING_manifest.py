from enum import Enum
from uuid import UUID, uuid3, uuid1
import graphviz

CTING_MANIFEST_VERSION = 0.1


UUID_DEFAULT = UUID('00000000-0000-0000-0000-000000000000')

#======================#
UUID_NAMESPACE_ATTACKFAMILIES = UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')
class AttackFamilies:
    uuid = UUID_DEFAULT

    name = ""
    descriptions = ""
    referenceLink = ""

    def GetFamiliesUuid(name):
        return uuid3(UUID_NAMESPACE_ATTACKFAMILIES, name)

    def __init__(self, name="", descriptions="", referenceLink=""):
        self.name = name
        self.uuid = AttackFamilies.GetFamiliesUuid(name)
        self.descriptions = descriptions
        self.referenceLink = referenceLink

#======================#
class HostType(Enum): # range from 0~0x10-1
    DEFAULT = 0

    HOST_WINDOWS = 1
    HOST_LINUX = 2

class AttackPatterns:
    uuid = UUID_DEFAULT

    # Descriptions
    attackFamilies = UUID_DEFAULT # corrsponding uuids
    descriptions = ""
    referenceLink = ""

    # Attack graphs
    targetHost = HostType.DEFAULT

    entitiesList = dict()
    activitiesList = dict()

    def GetPatternUuid(self, name):
        return uuid3(self.attackFamilies, name)

    def GetEntityUuid(self, eid=0, name=""):
        return uuid3(self.uuid, name + str(eid))

    def GetActivityUuid(self, sequenceNo=0):
        return uuid3(self.uuid, str(sequenceNo))

    # def GetPatternUuid(attackFamilies, name):
    #     uuid_attackFamilies = AttackFamilies.GetFamiliesUuid(attackFamilies)
    #     return uuid3(uuid_attackFamilies, name)

    def __init__(self, attackFamilies="", name="", descriptions="", referenceLink="", targetHost=HostType.DEFAULT):
        self.name = name
        self.attackFamilies = AttackFamilies.GetFamiliesUuid(attackFamilies)
        self.uuid = self.GetPatternUuid(name)
        self.descriptions = descriptions
        self.referenceLink = referenceLink
        self.targetHost = targetHost

    def addEnity(self, entity):
        if entity.uuid in self.entitiesList:
            print("Entity uuid: " + entity.uuid + " alread exists!")
        else:
            self.entitiesList[entity.uuid] = entity

        return entity.uuid

    def addActivity(self, activity):
        if activity.uuid in self.activitiesList:
            print("Activity uuid: " + activity.uuid + " alread exists!")
        else:
            self.activitiesList[activity.uuid] = activity
    
    def DrawGraph(self, graphName, graphType="png"):
        dot = graphviz.Digraph()

        for entity in self.entitiesList.values():
            entityShape = "box"
            if entity.types == EntityType.SUBJECT_PROCESS or entity.types == EntityType.SUBJECT_THREAD:
                entityShape = "ellipse"
            elif entity.types == EntityType.OBJECT_SOCKET:
                entityShape = "diamond"
            else:
                pass

            dot.node(name=str(entity.uuid).replace('\\','\\\\'), label=str(entity.eid).replace('\\','\\\\')+"\n"+entity.name.replace('\\','\\\\'), shape=entityShape)

        for activity in self.activitiesList.values():
            activityStyle = ""
            if activity.types == ActivityType.PERSISTENT_REGISTRY:
                activityStyle = "dashed"
                
            dot.edge(tail_name=str(activity.source), head_name=str(activity.destination), label=str(activity.sequenceNo), style=activityStyle)

        dot.format = graphType
        dot.render(graphName)

#======================#
class EntityType(Enum): # range from 0x10~0x100-1
    DEFAULT = 0x10 + 0

    # Subjects: range from 0x10~0x20-1, Shape: ellipse
    SUBJECT_PROCESS = 0x10 + 1
    SUBJECT_THREAD = 0x10 + 2
    # Objects: range from 0x20~0x100-1, Default Shape: box
    OBJECT_FILE = 0x10 + 0x10 + 1  # Shape: box
    OBJECT_SOCKET = 0x10 + 0x10 + 2 # Shape: diamond
    OBJECT_MEMORY = 0x10 + 0x10 + 3
    OBJECT_PIPELINE = 0x10 + 0x10 + 4
    OBJECT_REGISTRY = 0x10 + 0x10 + 5

class ActivityType(Enum): # range from 0x100~0x300-1
    # * -> * represent the information flow or control flow between system objects
    # range from 0x100~0x200-1
    DEFAULT = 0x100 + 0

    # Process & thread
    EVENT_CLONE = 0x100 + 1 # Subject -> Subject
    EVENT_EXECUTE = 0x100 + 2
    EVENT_CREATTHREAD = 0x100 + 3
    EVENT_WRITEMEMORY = 0x100 + 4

    # File | Registry
    EVENT_CREAT = 0x100 + 0x10 + 1 # Subject -> Object
    EVENT_WRITE = 0x100 + 0x10 + 2 # Write to an object
    EVENT_READ = 0x100 + 0x10 + 3 # Object -> Subject
    EVENT_LINK = 0x100 + 0x10 + 4
    EVENT_DELETE = 0x100 + 0x10 + 5

    # Network 
    EVENT_CONNECT = 0x100 + 0x20 + 1
    EVENT_SENDMSG = 0x100 + 0x20 + 2 # Subject -> Object
    EVENT_RECIVEMSG = 0x100 + 0x20 + 3 # Object -> Subject
    
    # Implied relationship
    # range from 0x200~0x300-1
    PERSISTENT_REGISTRY = 0x100 + 0x100 + 1

class Entity:
    uuid = UUID_DEFAULT
    types = EntityType.DEFAULT

    eid = 0 # processID, etc
    name = "" # file name/socket ip&port/registry name/process start command/...
    arguments = ""

    others = dict()

    # def GetEntityUuid(attackPatterns=UUID_DEFAULT, eid=0, name=""):
    #     return uuid3(attackPatterns, name + str(eid))

    def __init__(self, types, attackPatterns, eid=0, name="", arguments=""):
        self.types = types
        self.eid = eid # 0~0x7fff for process id (-1 for unknown process id)
        self.name = name
        self.uuid = attackPatterns.GetEntityUuid(eid, name)
        self.arguments = arguments

    def AddOthers(self, name, info):
        self.others[name] = info

class Activity:
    uuid = UUID_DEFAULT
    types = ActivityType.DEFAULT
    sequenceNo = 0

    source = UUID_DEFAULT
    destination = UUID_DEFAULT

    # def GetActivityUuid(attackPatterns=UUID_DEFAULT, sequenceNo=0):
    #     return uuid3(attackPatterns, str(sequenceNo))

    def __init__(self, types, attackPatterns, sequenceNo, source, destination):
        self.types = types
        self.sequenceNo = sequenceNo
        self.uuid = attackPatterns.GetActivityUuid(sequenceNo)
        self.source = source
        self.destination = destination
