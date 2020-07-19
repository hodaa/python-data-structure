class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None

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

            last_node.nextNode = new_node

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


linked_list = LinkedList()
linked_list.insert_start(1)
linked_list.insert_start(3)
linked_list.insert(2)
# print(linked_list.traverse())
# print(linked_list.get_size())
linked_list.remove(1)
linked_list.remove(2)
# linked_list.remove(3)
print(linked_list.traverse())
print(linked_list.get_size())
