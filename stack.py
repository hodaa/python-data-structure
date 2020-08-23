#python 3
items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])



# Enter your code here. Read input from STDIN. Print output to STDOUT
arr =[]
for _ in range(int(input())):
    process = input().split()
    if int(process[0])==1:
        arr.append(int(process[1]))
    if int(process[0])==2:
        del arr[-1]
    if int(process[0])==3:
        print(arr[-1])
