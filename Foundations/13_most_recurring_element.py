# Approach: Store all the occurrence of elements in dict and return with max frequency

def most_recurring(nums):
    dict = {}
    for ele in nums:
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele] = 1
    return max(dict.keys(),key=dict.get)

ans = most_recurring([1,2,3,4,5,5,5,5,5,5,5,5,5,5,2,23,3,4,4,4,4])
print(ans)