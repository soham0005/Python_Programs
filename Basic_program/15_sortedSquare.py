'''
Given an array return an array of the elements squared in sorted order

'''
def squareSorted(arr):
    result  = []
    for ele in arr: 
        result.append(ele**2)
    return sorted(result)


ans = squareSorted([-4,-1,0,3,10])
print(ans)