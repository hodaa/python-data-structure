class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue==[]

    def dequeue(self):
        if not self.queue:
            return  "stack is empty"

        last_item = self.queue[0]
        del self.queue[0]
        return last_item


    def enqueue(self,item):
        self.queue.append(item)

    def peek(self):
        if not self.queue:
            return  "stack is empty"

        return  self.queue[0]

    def get_size(self):
        return len(self.queue)



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
print(queue.get_size())
print(queue.dequeue())

# stack.traverse()



