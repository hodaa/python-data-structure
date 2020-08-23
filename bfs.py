class Node():
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.adjacentList= []



class BFS:

    #Breadth first search use queue DFS use stack or recursion
    def traverse(self,startNode):
        queue= [startNode]
        startNode.visited = True

        while queue:
            node = queue.pop(0)
            print(node.data)

            for n in node.adjacentList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)






node1= Node("A")
node2= Node("B")
node3= Node("C")
node4= Node("D")
node5= Node("E")

node1.adjacentList.append(node2)
node1.adjacentList.append(node4)
node2.adjacentList.append(node3)
node2.adjacentList.append(node5)

bfs= BFS()
bfs.traverse(node1)












