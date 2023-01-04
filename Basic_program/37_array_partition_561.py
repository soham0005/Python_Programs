def arrayPairs(nums):
    nums.sort()
    result = 0
    for i in range(0,len(nums),2):
        result += nums[i]
    return result

ans = arrayPairs([1,3,4,2])
print(ans)