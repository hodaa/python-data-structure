class Node(object):
    def __init__(self,data):
        self.left_node = None
        self.right_node =None
        self.data = data
        self.height = 0

class AVL(object):
    def __init__(self):
        self.root = None

    def get_height(self,node):
        if not node:
            return -1
        return node.height

    #if >1 right rotation
    #if <-1 left rotation
    def check_balanced(self,node):

        if not node:
            return 0

        return self.get_height(node.left_node) - self.get_height(node.right_node)


    def rotate_right(self,node):
        print("rotate left on node", node.data)
        temp_left_child= node.left_node
        t=temp_left_child.right_node

        temp_left_child.right_node= node
        node.left_node=t

        node.height= max(self.get_height(node.left_node),self.get_height(node.right_node))+1
        temp_left_child.height= max(self.get_height(temp_left_child.left_node),self.get_height(temp_left_child.right_node))+1

        return  temp_left_child

    def  rotate_left(self,node):
        print("rotate left on node", node.data)
        temp_right_child= node.right_node
        t=temp_right_child.left_node
        #
        temp_right_child.right_node= node
        node.right_node=t
        #
        node.height= max(self.get_height(node.left_node),self.get_height(node.right_node))+1
        temp_right_child.height= max(self.get_height(temp_right_child.left_node),self.get_height(temp_right_child.right_node))+1

        return  temp_right_child

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
           return self.insert_node(self.root,data)

    def insert_node(self,node,data):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_node = self.insert_node(node.left_node,data)

        if data > node.data:
            node.right_node = self.insert_node(node.right_node, data)

        node.height= max(self.get_height(node.left_node),self.get_height(node.right_node)) + 1
        return  self.settleViolation(data,node)


    def settleViolation(self,data,node):
        print("in settle",data,node.data);
        balance = self.check_balanced(node)
        print ("balance",balance)

        # case1: left left heavy situation
        if balance > 1  and data < node.left_node.data:
            print("left left heavy situation")
            return self.rotate_right(node)

        if balance > 1 and data > node.left_node.data:
            print("Left right heavy situation")
            node.left_node= self.rotate_left(node.left_node)
            return self.rotate_right(node)


        #case2 : right right heavy situation
        if balance < -1 and data > node.right_node.data:
            print("Right right heavy situation ..")
            return self.rotate_left(node)

        if balance < -1 and data < node.right_node.data:
            print("Right left heavy situation ..")
            node.right_node= self.rotate_right(node.right_node)
            return self.rotate_left(node)

        return node

    def travers_in_order(self):
        if self.root:
            self.travers_in_order_node(self.root)

   private def travers_in_order_node(self,node):
        if node.left_node:
             self.travers_in_order_node(node.left_node)

        print(node.data)

        if node.right_node:
            self.travers_in_order_node(node.right_node)



av= AVL()
av.insert(5)
av.insert(3)
av.insert(4)
av.travers_in_order()



















