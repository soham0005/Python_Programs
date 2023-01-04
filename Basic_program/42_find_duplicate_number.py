# def findDuplicate(nums):
#     for i in range(len(nums)):
#         index = abs(nums[i])

#         if(nums[index]>0):
#             nums[index] = -nums[index]
#         else:
#             return index


def findDuplicate(nums):
    for i in range(len(nums)):
        index = abs(nums[i])
        if(nums[index]>0):
            nums[index] = -nums[index]
        else:
            return index
ans = findDuplicate([1,3,4,2,2])
print(ans)