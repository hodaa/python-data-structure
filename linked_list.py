class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.index= 0


class LinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None
        self.index= 0

    def reverse(self):
        prev = None
        current = self.head
        index =self.size-1
        while current is not None:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            #
            current.index = index
            index -=1
            #
            current = next



        #
        self.head = prev


        # 0(1)
    def insert_start(self, data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def get_size(self):
        return self.size

    def count(self):
        size = 0
        node = self.head

        while node is not None:
            size += 1
            node = node.nextNode
        return size

    def insert(self, data):

        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            last_node = self.head
            while last_node.nextNode is not None:
                last_node = last_node.nextNode
                self.index +=1

            last_node.nextNode = new_node
            last_node.index = self.index


    def traverse(self):
        this_node = self.head
        while this_node is not None:
            print('%d' % this_node.data)
            this_node = this_node.nextNode

    def remove(self, data):
        if self.head is None:
            return

        self.size -= 1
        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.nextNode

        if previous_node is None:
            self.head = current_node.nextNode
        else:
            previous_node.nextNode = current_node.nextNode

    def getNodeIndex(self,node):
        current = self.head
        while current is not None:
            if current.data  == node:
                return current.index

            current = current.nextNode

    def getNodeValue(self, index):
        current = self.head
        while current is not None:
            if current.index == index:
                return current.data

            current = current.nextNode

    def test(self):
        Node.right="hoda";


linked_list = LinkedList()
# linked_list.insert_start(1)
# linked_list.insert_start(2)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

# print(linked_list.traverse())
# print(linked_list.get_size())
# linked_list.remove(1)
# linked_list.remove(2)
# linked_list.remove(3)
# linked_list.traverse()
linked_list.reverse()
# linked_list.traverse()
print(linked_list.getNodeIndex(1))
print(linked_list.getNodeValue(2))
linked_list.test()
# print(linked_list.get_size())
