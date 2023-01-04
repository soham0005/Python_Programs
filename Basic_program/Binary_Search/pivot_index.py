'''
Problem Statement:- Find the index in the array where rotation is occured.
'''
import math

def pivotIndex(arr):
    start = 0
    end = len(arr) - 1
    mid = math.floor(start + (end - start)/2)

    while(start< end):
        if(arr[mid] >= arr[0]):
            start = mid + 1
        else:
            end = mid
        mid = math.floor(start + (end - start)/2)
        
    return start
        

ans = pivotIndex([12,1,2,3,4])
print(ans)