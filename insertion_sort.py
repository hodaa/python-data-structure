#inserting an element at a particular position
#O(n*n) sorting algorithms
#stable
#in space
#require more writes

def insertion_sort(arr):
    for i in range(1,len(arr)):
        decrement = i-1
        value = arr[i]
        while(value<arr[decrement] and decrement >= 0):
            arr[decrement+1]= arr[decrement]
            decrement -=1
        arr[decrement+1] = value
    return arr

print(sortMe([12,11,13,5,6]))
