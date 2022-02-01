 #o(N*N) // find the smallest  item  in the array
 # not stable
def sortMe(arr): 
    i =0;
    while  i<len(arr) :
        m = min(arr[i:])
        arr.remove(m)
        arr.insert(i,m)
        i+=1
       
    return arr
  


print(sortMe([64, 25, 12, 22, 11]))
print(sortMe(['paper', 'true' , 'soap' ,'floppy', 'flower']))

# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1) 