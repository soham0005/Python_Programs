def duplicate_number_2(nums):
    obj = {}
    for ele in nums:
        if ele in obj:
            
            obj[ele]+=1
        else:
            obj[ele] = 1
    
    for key,value in obj.items():
        if value == 1:
            return key
ans = duplicate_number_2([2,2,3,2])
print(ans)