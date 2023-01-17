def rotateArray(nums,k):
    n = len(nums)
    temp = nums[:]

    for i in range(0,n):
        ele = (i+k) % n
        nums[ele] = temp[i]

    return nums

ans =  rotateArray([1,2,3,4,5,6],3)
print(ans)