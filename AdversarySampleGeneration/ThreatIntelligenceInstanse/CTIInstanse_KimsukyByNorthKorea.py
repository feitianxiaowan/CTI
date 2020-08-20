from AdversarySampleGeneration.ThreatIntelligenceInstanse.CTING_manifest import *

from uuid import uuid3
import os


Family_Kimsuky = AttackFamilies(name="Kimsuky", referenceLink="https://www.freebuf.com/articles/network/233629.html")

Pattern_Kimsuky2020 = AttackPatterns(name="Kimsuky2020", attackFamilies="Kimsuky", targetHost=HostType.HOST_WINDOWS)

# uuid_attackPatterns = Pattern_Kimsuky2020.GetPatternUuid(name="Kimsuky2020")
activityCount = 0

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.OBJECT_FILE, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid="*\\", 
    name="*.scr"))

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid=-1, 
    name="*.scr"))    

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_EXECUTE, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid="*\\", name="*.scr"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="*.scr")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid=-1, 
    name="regsv*.exe"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREAT, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="*.scr"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="regsv*.exe")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.OBJECT_FILE, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid="%AppData%\\Roaming\\Microsoft\\Windows\\Defender\\", 
    name="AutoUpdate.dll"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREAT, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="regsv*.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="%AppData%\\Roaming\\Microsoft\\Windows\\Defender\\", name="AutoUpdate.dll")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.OBJECT_REGISTRY, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid="HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\WindowsDefender", 
    name="regsvr*32.exe /s %AppData%\\Roaming\\Microsoft\\Windows\\Defender\\AutoUpdate.dll"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREAT, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="regsv*.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\WindowsDefender", name="regsvr*32.exe /s %AppData%\\Roaming\\Microsoft\\Windows\\Defender\\AutoUpdate.dll")))
activityCount += 1

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.PERSISTENT_REGISTRY, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid="HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\WindowsDefender", name="regsvr*32.exe /s %AppData%\\Roaming\\Microsoft\\Windows\\Defender\\AutoUpdate.dll"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="%AppData%\\Roaming\\Microsoft\\Windows\\Defender\\", name="AutoUpdate.dll")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.OBJECT_FILE, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid="%AppData%\\Local\\Temp\\",
    name="*.tmp.bat"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREAT, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="regsv*.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="%AppData%\\Local\\Temp\\",name="*.tmp.bat")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid=-1, 
    name="*.tmp.bat"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_EXECUTE, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid="%AppData%\\Local\\Temp\\",name="*.tmp.bat"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="*.tmp.bat")))
activityCount += 1

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_DELETE, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="*.tmp.bat"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="*\\", name="*.scr")))
activityCount += 1

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_DELETE, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="*.tmp.bat"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="%AppData%\\Local\\Temp\\",name="*.tmp.bat")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid=-1, 
    name="RunServices.exe"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_READ, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid="HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\WindowsDefender", name="regsvr*32.exe /s %AppData%\\Roaming\\Microsoft\\Windows\\Defender\\AutoUpdate.dll"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="RunServices.exe")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid=-1, 
    name="Explorer.exe"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_WRITEMEMORY, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="RunServices.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="Explorer.exe")))
activityCount += 1

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREATTHREAD, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="RunServices.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="Explorer.exe")))
activityCount += 1

Pattern_Kimsuky2020.addEnity(Entity(
    types=EntityType.OBJECT_SOCKET, 
    attackPatterns=Pattern_Kimsuky2020, 
    eid="", 
    name="suzuki.datastore.pe.hu"))

Pattern_Kimsuky2020.addActivity(Activity(
    types=ActivityType.EVENT_CREATTHREAD, 
    attackPatterns=Pattern_Kimsuky2020, 
    sequenceNo=activityCount, 
    source=Pattern_Kimsuky2020.GetEntityUuid(eid=-1, name="Explorer.exe"), 
    destination=Pattern_Kimsuky2020.GetEntityUuid(eid="", name="suzuki.datastore.pe.hu")))
activityCount += 1

if __name__ == '__main__':
    Pattern_Kimsuky2020.DrawGraph(graphName="Kimsuky2020.Instanse")
    os.system('dot -Tpng -O .\\Kimsuky2020.Instanse')
    pass
