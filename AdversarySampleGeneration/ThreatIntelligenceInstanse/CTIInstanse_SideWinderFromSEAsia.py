from AdversarySampleGeneration.ThreatIntelligenceInstanse.CTING_manifest import *

from uuid import uuid3
import os

Family_SideWinder = AttackFamilies(name="SideWinder", referenceLink="https://ti.qianxin.com/blog/articles/the-recent-rattlesnake-apt-organized-attacks-on-neighboring-countries-and-regions/, http://it.rising.com.cn/dongtai/19658.html")

Pattern_SideWinder2020 = AttackPatterns(name="SideWinder2019", attackFamilies="SideWinder", targetHost=HostType.HOST_WINDOWS)

activityCount = 0

node1 = Pattern_SideWinder2020.addEnity(Entity(
    types=EntityType.OBJECT_FILE, 
    attackPatterns=Pattern_SideWinder2020, 
    eid="*\\", 
    name="Policy Guidelines for Online Classes.lnk"))

node2 = Pattern_SideWinder2020.addEnity(Entity(
    types=EntityType.SUBJECT_PROCESS, 
    attackPatterns=Pattern_SideWinder2020, 
    eid="c:\\windows\\system32\\", 
    name="cmd.exe",
    arguments=' /c start /wait "YDthZQ" C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\temp_file_name.Ink'))

Pattern_SideWinder2020.addActivity(Activity(
    types=ActivityType.EVENT_EXECUTE, 
    attackPatterns=Pattern_SideWinder2020, 
    sequenceNo=activityCount, 
    source=node1, 
    destination=node2))
activityCount += 1

node3 = Pattern_SideWinder2020.addEnity(Entity(
    types=EntityType.OBJECT_SOCKET, 
    attackPatterns=Pattern_SideWinder2020, 
    eid="", 
    name="http://www.au-edu.km01s.net/images/E2BC769A/16914/..."))

Pattern_SideWinder2020.addActivity(Activity(
    types=ActivityType.EVENT_CONNECT, 
    attackPatterns=Pattern_SideWinder2020, 
    sequenceNo=activityCount, 
    source=node2, 
    destination=node3))
activityCount += 1

Pattern_SideWinder2020.addActivity(Activity(
    types=ActivityType.EVENT_RECIVEMSG, 
    attackPatterns=Pattern_SideWinder2020, 
    sequenceNo=activityCount, 
    source=node3, 
    destination=node2))
activityCount += 1



if __name__ == '__main__':
    Pattern_SideWinder2020.DrawGraph(graphName="SideWinder2020.Instanse")
    os.system('echo "dot -Tpng -O .\\SideWinder2020.Instanse" | pwsh')
    pass
