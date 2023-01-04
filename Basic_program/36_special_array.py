def special_array(nums):
    result = -1 
    maxVal = max(nums)

    for i in range(maxVal+1):
        val = len([x for x in nums if x>=i])
        if val == i:
            result = max(val,result)
    return result

ans = special_array([0,4,3,0,4])
print(ans)