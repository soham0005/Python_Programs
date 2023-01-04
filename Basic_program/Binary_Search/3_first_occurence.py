import math

def first_occurence(arr,target):
    start = 0
    end = len(arr) - 1
    pos = -1

    while(start<=end):
        mid = math.floor(start + (end - start)/2)
        
        if arr[mid] == target:
            pos = mid
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return pos

ans = first_occurence([1,2,3,3,3,3,3,5,6,7,8,8,8,8,8,8],8)
print(ans)
