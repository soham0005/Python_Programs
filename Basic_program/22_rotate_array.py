def rotateArray(nums,k):
    temp = nums.copy()
    n = len(nums)
    for i in range(0,n):
        ele = (i+k) % n
        nums[ele] = temp[i]


    print(nums)
rotateArray([1,2,3,4,5,6,7],3)