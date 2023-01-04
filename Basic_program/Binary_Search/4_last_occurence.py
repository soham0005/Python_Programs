import math
def last_occurrence(arr,target):
     
    start = 0
    end = len(arr) - 1
    pos = -1
    while(start<=end):
        mid = math.floor(start+(end-start)/2)
        if arr[mid] == target:
            pos = mid
            start = mid+1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    mid = math.floor(start+(end-start)/2)

    return pos


ans = last_occurrence([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,6,7,7,8,98],3)
print(ans)