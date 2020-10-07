#!/home/zhenyuan/anaconda3/envs/cti/bin/python

from DataPreprocess.DarpaE5Trace import DarpaE5TraceParser
from GraphStorageReproduction.VertexCentricRDB import *


def main():
    # DarpaE5TraceParser().BasicParser()
    cdb = VertexCentricRDB()
    cdb.ReadFromDarpaE5Trace()
    pass


if __name__ == '__main__':
    main()
