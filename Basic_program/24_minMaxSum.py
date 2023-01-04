def minMaxSum(arr):
    minEle = min(arr)
    maxEle = max(arr)
    return minEle+maxEle


ans = minMaxSum([1,2,3,4,5,2,1,3])
print(ans)