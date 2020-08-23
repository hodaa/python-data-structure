class Node(object):
    def __init__(self,data):
        self.data = data
        self.right_node = None
        self.left_node = None


class BinaryTree(object):
    def __init__(self):
        self.root = Node(1)

    def insert(self, left_data, right_data, i):
        self.insertNode(left_data, right_data ,self.root, i)

    def insertNode(self, left_data,right_data, root_node,i):

        if not root_node.left_node and not root_node.right_node:
            root_node.left_node = Node(left_data)
            root_node.right_node = Node(right_data)
            
        elif i % 2 != 0 & i !=0:
            self.insertNode(left_data,right_data,root_node.left_node,i)

        elif i % 2 == 0 & i != 0:
            self.insertNode(left_data,right_data,root_node.right_node,i)


    def traverse(self):
        if self.root is not None:
            self.traversInOrder(self.root)

    def traversInOrder(self, node):
        if node.left_node:
            self.traversInOrder(node.left_node)

        print(node.data)

        if node.right_node:
            self.traversInOrder(node.right_node)

print(2%1)
print(2%2)
print(2%3)
# bn = BinaryTree()
# bn.insert(2,3,0)
# bn.insert(4,5,1)
# bn.insert(6,7,2)
# bn.traverse();

# for i in range(3):
#     self.insert(input[0],input[1],i)



# 3
# 2 3
# -1 -1
# -1 -1
# 2
# 1
# 1