class MaxHeap(object):
    HEAP_SIZE=10

    def __init__(self):
        self.currentPosition = -1
        self.heap =[0]*self.HEAP_SIZE


    def insert(self,item):
        if self.isFull():
            print("The Heap is full")
            return
        self.currentPosition+=1
        self.heap[self.currentPosition] =item
        self.fixUp(self.currentPosition)



    def isFull(self):
        if self.currentPosition == self.HEAP_SIZE:
            return  True
        return  False

    def fixUp(self,index):
        parentIndex =int((index-1)/2)
        while parentIndex >=0 and  self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            # parentIndex = int((index - 1) / 2)

    def list(self):
        print(self.currentPosition)
        print(self.heap[self.currentPosition])

        print(self.heap)


from sys import stdin
from heapq import heappush, heappop

heap = []
item_lookup = set()


def push(v):
    heappush(heap, v)
    item_lookup.add(v)


def discard(v):
    item_lookup.discard(v)


def print_min():
    while heap[0] not in item_lookup:
        heappop(heap)

    print
    heap[0]


cmds = {
    1: push,
    2: discard,
    3: print_min
}

n = int(stdin.readline())
for _ in range(n):
    data = map(int, stdin.readline().split(" "))
    cmds[data[0]](*data[1:])




heap =MaxHeap()
heap.insert(11)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(10)
heap.list()












