def majorityElement(nums):
        dict = {}
        for num in nums:
            if dict.get(num) == None:
                dict[num] = 1
            else:
                dict[num] += 1
        return max(dict.keys(), key=dict.get)
ans = majorityElement([2,2,2,2,4,4,4,4,4])
print(ans)