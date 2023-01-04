def repeating_element(nums):
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            return index 
ans = repeating_element([1,2,11,3,4,5,6,7,8,9,10,10])
print(ans)