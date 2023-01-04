import math
def binarySearch(arr,target):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = math.floor(start + (end - start)/2)

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    
    return False

ans = binarySearch([2,3,4,5,6,7,8],2)
print(ans)