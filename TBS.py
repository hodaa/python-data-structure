class Node(object):
    def __init__(self , character):
        self.character = character
        self.left_node = None
        self.right_node= None
        self.middle_node = None
        self.value= None

class TST():

    def __init__(self):
        self.root = None

    def put(self,key,value):
            self.root = self.putItem(self.root,key,value,0)

    def putItem(self, node, key, value, index):
        if node is None:
            node = Node(key[index])

        if  key[index] < node.character  :
            node.left_node = self.putItem(node.left_node, key, value, index)
        elif key[index] > node.character:
            print(key[index])
            node.right_node = self.putItem(node.right_node, key, value, index)
        elif index < len(key)-1:
            node.middle_node = self.putItem(node.middle_node, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self,key):
        node = self.getItem(self.root,key,0)
        if node is not None:
            return node.value
        else:
            return "return not exists"


    def getItem(self, node, key, index):
        if node is None:
            return None
        if index < len(key)-1:
            return self.getItem(node.middle_node,key,index+1)
        elif  key[index] < node.character:
            return self.getItem(node.left_node,key,index)
        elif key[index] > node.character:
            return self.getItem(node.right_node,key,index)
        else:
            return node

    def getIndex(self,key):
        if self.root is not None:
            return self.getCharacterIndex(self.root,key,0,-1)


    def getCharacterIndex(self,node,key,index,count):
        if index <= len(key)-1:
            if node is None:
                return 0
            elif key[index] == node.character:
                count+=1
                return self.getCharacterIndex(node.middle_node,key,index+1,count)
            elif key[index] > node.character:
                return self.getCharacterIndex(node.right_node, key, index,count)
            elif key[index] < node.character:
                return self.getCharacterIndex(node.left_node, key, index,count)


        return count




tbs= TST()
# tbs.put('car',20)
tbs.put('hack',30)
tbs.put('hackerrank',100)
print(tbs.getIndex('haK'))
# print(tbs.get('hak'))

