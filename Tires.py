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

    def put(self,key):
            self.root = self.putItem(self.root,key,0)

    def putItem(self, node, key, index):
        if node is None:
            node = Node(key[index])

        if  key[index] < node.character  :
            node.left_node = self.putItem(node.left_node, key, index)
        elif key[index] > node.character:
            print(key[index])
            node.right_node = self.putItem(node.right_node, key,  index)
        elif index < len(key)-1:
            node.middle_node = self.putItem(node.middle_node, key, index+1)

        return node


    def find(self,key):
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
tbs.put('s')
tbs.put('ss')
tbs.put('sss')
tbs.put('ssss')
tbs.put('sssss')
print(tbs.find('s'))

