def missingNumber(nums):
    for i in range(len(nums)+1):
        if i not in nums:
            return i

ans = missingNumber([1,2,3,4,2,1,34,1,12])
print(ans)