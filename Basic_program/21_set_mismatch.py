from collections import defaultdict

def setmistMatch(nums):
    result = [0,1]
    nums.sort()

    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            result[0] = nums[i]
        elif nums[i]> nums[i-1]+1:
            result[1] = nums[i-1]+1
    
    if(nums[len(nums)-1]!=len(nums)):
        result[1] = len(nums)
    return result


ans = setmistMatch([1,1])
print(ans)