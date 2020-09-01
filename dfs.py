class Node(object):
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjacentList= []


class DFS(object):

    def traverse(self, node): #layer by layer algorithme
        node.visited= True
        print(node.data)

        for n in node.adjacentList:
            if not n.visited:
                self.traverse(n)


node1= Node("A")
node2= Node("B")
node3= Node("C")
node4= Node("D")
node5= Node("E")

node1.adjacentList.append(node2)
node1.adjacentList.append(node4)
node2.adjacentList.append(node3)
node2.adjacentList.append(node5)
#
dfs= DFS()
dfs.traverse(node2)





