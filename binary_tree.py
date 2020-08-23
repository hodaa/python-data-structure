class Node(object):
    def __init__(self,data):
        self.data= data
        self.right_node = None
        self.left_node = None


class BinaryTree(object):

    def __init__(self):
        self.root = None


    def insert (self,data):
        if not self.root:
           self.root=Node(data)
        else:
            self.insertNode(data, self.root)


    #O(Log N)
    def insertNode(self, data, root_node):
        if data < root_node.data:
            if not root_node.left_node:
                root_node.left_node= Node(data)
            else:
               self.insertNode(data,root_node.left_node)
        else:
            if not root_node.right_node:
                root_node.right_node =  Node(data)
            else:
                self.insertNode(data, root_node.right_node)


## iteratve solution
    def insert(self, val):
        cur = self.root
        if not cur:
            self.root = Node(val)
            return self.root

        while cur:
            if cur.info > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break

        return self.root


    def traverse_min(self):
        if self.root:
            return  self.get_node_min(self.root)


    def get_node_min(self,node):
         if node.left_node:
             return self.get_node_min(node.left_node)
         else:
             return node.data


    def traverse_max(self):
        if self.root:
            return self.get_node_max(self.root)

    def get_node_max(self, node):
        if node.right_node:
            return self.get_node_max(node.right_node)
        else:
            return node.data


    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)


    def traverse_in_order(self,node):

        if node.right_node:
            self.traverse_in_order(node.right_node)

        print(node.data)

        if node.left_node:
            self.traverse_in_order(node.left_node)


    def traverse_pre_order(self):
        if self.root:
            self.traverse_node_pre_order(self.root)

    def traverse_node_pre_order(self, node):
        print(node.data)

        if node.left_node:
            self.traverse_node_pre_order(node.left_node)

        if node.right_node:
            self.traverse_node_pre_order(node.right_node)


    def remove(self, data):
        if self.root: # tree not empty
           return self.remove_node(self.root, data)

    def remove_node(self, node, data):
        if data < node.data:
            node.left_node = self.remove_node(node.left_node, data)

        elif data > node.data:
            node.right_node = self.remove_node(node.right_node,data)

        else:
            if not node.left_node and  not node.right_node:
                del node
                return None

        return node


tree= BinaryTree()
tree.insert(5)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(9)
tree.insert(8)
tree.traverse();
# print(tree.height())


