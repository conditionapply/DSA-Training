def replace(arr):
    n = len(arr)
    maxR =-1
    for i in range(n-2,-1,-1):
        temp =arr[i]
        arr[i]= maxR
        maxR =max(maxR,temp)
    return arr
arr = [17,18,5,4,6,1]
print(replace(arr))