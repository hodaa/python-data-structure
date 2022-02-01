#Quick sort is not a stable
#The average case space used will be of the order O(log n)
#The worst case space used will be O(n)

def quick_sort(arr,low, high):
    if  low < high:
        pivot= partion(arr,low,high)
        print(pivot)

        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

    return arr


def partion(arr,low,high):
    i = low
    pivot= arr[high]
    for j in  range(low,high):
        # print(j)
        if arr[j]< arr[high]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high] = arr[high],arr[i]
    return i



# print(quick_sort([23,6,4,-1,0,12,8,3,1],0,8))
print(quick_sort([2,1,3],0,2))