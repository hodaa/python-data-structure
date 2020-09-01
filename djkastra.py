import sys;
import heapq;

class Edge(object):
    def __init__(self,weight, startVertex,targetVertex):

        self.weight= weight
        self.startVertex =startVertex
        self.targetVertex =targetVertex


class Node(object):
    def __init__(self, name):
        self.name=name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList =[]
        self.minDistance = sys.maxsize


class Djkastra:
