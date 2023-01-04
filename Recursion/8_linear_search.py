def linearSearch(arr,key,size):
    if size == 0:
        return False
    if arr[size] == key:
        return True
    else:
        return linearSearch(arr,key,size-1)

array = [1,2,3,4,2,4,2,1,3,1,1,10,20] 
key = 201
size = len(array)-1
ans = linearSearch(array,key,size)
print(ans)