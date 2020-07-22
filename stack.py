class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack==[]

    def pop(self):
        if not self.stack:
            return  "stack is empty"

        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item


    def push(self,item):
        self.stack.append(item)

    def peek(self):
        if not self.stack:
            return  "stack is empty"

        return  self.stack[-1]

    def get_size(self):
        return len(self.stack)



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_size())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())

# stack.traverse()



