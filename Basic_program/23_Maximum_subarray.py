def maxSum(nums): 
    import sys
    maxsum = -sys.maxsize-1
    sum = 0
    for i in range(0,len(nums)):
        sum = max(nums[i],nums[i]+sum)
        maxsum = max(sum,maxsum)
    return maxsum
 
ans = maxSum([1])
print(ans)