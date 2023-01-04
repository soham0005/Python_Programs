def unique_number(nums):
    unique = 0
    for i in nums:
        unique ^= i
    return unique

ans = unique_number([4,1,2,1,2])
print(ans)