#Bubble sort is a stable algorithm
# A sorting algorithm is said to be stable if two objects with equal keys appear in the same order 
#in sorted output as they appear in the input array to be sorted.
# Bubble sort is an in place algorithm:  does not need an extra space memory
#O(n*n) sorting algorithms

def sortMe(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1): #the largest element is bubbled towards the right most position
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    print("--------------")
    return arr

# print(sortMe([1,2,3,4,5,6,7,8,9]))
print(sortMe([8,5, 1, 4, 2]))
# print(sortMe([]))
