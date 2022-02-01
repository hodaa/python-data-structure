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
                self.insertNode(data,root_node.right_node)


## iteratve solution
    # def insert(self, val):
    #     cur = self.root
    #     if not cur:
    #         self.root = Node(val)
    #         return self.root
    #
    #     while cur:
    #         if cur.info > val:
    #             if cur.left:
    #                 cur = cur.left
    #             else:
    #                 cur.left = Node(val)
    #                 break
    #         else:
    #             if cur.right:
    #                 cur = cur.right
    #             else:
    #                 cur.right = Node(val)
    #                 break
    #
    #     return self.root


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


    def traverse_ancestors(self,target):
        if self.root:
            self.traverse_in_order_anc(self.root,target)




    def traverse_in_order_anc(self,node,target):
        if target < node.data:
            self.traverse_in_order_anc(node.left_node,target)
            print(node.data)
        if target > node.data:
            self.traverse_in_order_anc(node.right_node,target)
            print(node.data)



    
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
    

    # return all ancestors
    # def get_ancestors(self,root,target):
    #     node = Node(root)
    #     if node is None:
    #         return false
    #     if node.data == target:
    #         return true
    #     elif target < node.data:
    #         self.get_ancestors(node.left_node,target)
        #     # print(node.data)
        # elif target > node.data:
        #     get_ancestors(self,node.right_node,target)
        # print(node.data)

    def invert(self):
        self.invert_node(self.root)
    
        def invert_node(self,node):
            if node.right_node and node.left_node:
                self.invert_node(node.left_node)
                self.invert_node(node.right_node)
                node.left_node,node.right_node=node.right_node,node.left_node
        # if node.left_node and node.right_node is None:
        #     self.invert_node(node.left_node)
        #     # node.right_node = None
        #     node.right_node = node.left_node
        # if node.right_node and node.left_node is None:
        #     self.invert_node(node.right_node)
        #     node.left_node = node.right_node
        # else:
        #     return
        # if node.right:
        #     self.invert_node(node.right)
        #     if node.left:
        #         node.left,node.right = node.right, node.right
        # if node.left:
        #     self.invert_node(node.left)

        
        
       




tree= BinaryTree()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)
tree.traverse_pre_order()
print("---------------")
tree.invert()
tree.traverse()
# tree.traverse_ancestors(1)
# tree.traverse_in_order()
# tree.get_ancestors(5,1)
# print(tree.height())


