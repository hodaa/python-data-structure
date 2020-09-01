class MinHeap(object):
    def __init__(self):
        self.heap =[]
        self.currentPosition = -1

    def insert(self,item):
        self.currentPosition +=1
        self.heap.append(item)
        self.fixUp(self.currentPosition)

    def fixUp(self,index):
        parentIndex = int((index-1)/2)
        while parentIndex >=0  and  self.heap[index] < self.heap[parentIndex]:
            temp =  self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] =temp
            parentIndex = int((index - 1) / 2)

    def remove(self,item):
        index_deleted = self.heap.index(item)
        self.heap[index_deleted] = self.heap[-1]
        del self.heap[-1]
        self.fixUp(self.heap.index(self.heap[-1]))



    def list(self):
        print(self.heap)



minHeap =MinHeap()
minHeap.insert(4)
minHeap.insert(30)
minHeap.insert(9)
minHeap.insert(18)
minHeap.insert(19)
print(minHeap.list())
minHeap.remove(4)
print(minHeap.list())



