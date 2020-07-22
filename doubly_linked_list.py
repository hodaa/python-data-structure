class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextRef = None
        self.previousRef = None


class DoublyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.start_node =None


    # 0(1)
    def insert_start(self, data):
        self.size += 1

        newNode = Node(data)
        if not self.start_node:
            self.start_node = newNode
        else:
           print("list is not empty")


    def get_size(self):
        return self.size

    def count(self):
        size = 0
        node = self.head

        while node is not None:
            size += 1
            node = node.nextNode
        return size

    def insert_at_start(self, data):

        self.size += 1
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node

        else:
            new_node.nextRef = self.start_node
            self.start_node.previousRef=new_node;
            self.start_node = new_node



    def insert_at_end(self, data):

        new_node = Node(data)
        if self.start_node is None:  # is empty
            self.start_node = new_node
            return

        last_node = self.start_node
        while last_node.nref is not None:
            last_node = last_node.nref

        last_node.nextRef = new_node
        new_node.pref = last_node


    def traverse(self):

        this_node = self.start_node
        while this_node is not None:
            print('%d' % this_node.data)
            this_node = this_node.nextRef


    def delete_element_by_value(self, data):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        if self.start_node.nref is None:
            if self.start_node.data == data:
                self.start_node = None
            else:
                print("Item not found")
            return

        if  self.start_node.item == data:
            self.start_node = self.start_node.nref
            self.start_node.pref = None

            return




double_list =DoublyLinkedList ()
double_list.insert(1)
double_list.insert(2)

print(double_list)
