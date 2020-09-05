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

    def __cmp__(self, other):
        return self.cmp(self.minDistance,other.minDistance)

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


class Djkastra(object):

    def calcShortestPath(self, startVertex):
        q= []
        startVertex.minDistance= 0
        heapq.heappush(q, startVertex)
        while len(q):
            actualVertex= heapq.heappop(q)
            for edge in actualVertex.adjacenciesList:
                s = edge.startVertex
                t = edge.targetVertex
                newDistance= s.minDistance + edge.weight

                if int(newDistance) < int(t.minDistance):
                    t.predecessor= s
                    t.minDistance = newDistance
                    heapq.heappush(q,t)


    def getShortestPath(self,targetVartex):
        print("Shortest Path is " ,targetVartex.minDistance)
        node = targetVartex
        while node:
            print('%s' % node.name)
            node =node.predecessor



node1= Node("A")
node2= Node("B")
node3= Node("C")
node4= Node("D")
node5= Node("E")
node6= Node("F")
node7= Node("G")
node8= Node("H")

edge1= Edge(5,node1,node2)
edge2= Edge(9,node1,node5)
edge3= Edge(8,node1,node8)
edge4= Edge(15,node2,node4)
edge5= Edge(12,node2,node3)
edge6= Edge(4,node2,node8)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge5)
node2.adjacenciesList.append(edge4)

vertexList= (node1, node2, node3, node4, node5, node6, node7, node8)
dij= Djkastra()
dij.calcShortestPath(node1)
dij.getShortestPath(node4)

