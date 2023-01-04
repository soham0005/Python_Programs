def isSorted(arr,size):
    if size == 0 or size == 1:
        return True
    if arr[size-1]<arr[size-2]:
        return False
    return isSorted(arr,size-1)

array = [1,2,3,7,5,6]
size = len(array)
ans = isSorted(array,size)
print(ans)