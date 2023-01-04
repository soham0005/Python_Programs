'''
Universal Two Sum using map/dictionary:-
'''
def twoSum(arr,target):
    map = {}
    
    for i in range(len(arr)):
        ele = target - arr[i]
        if ele not in map:
            map[arr[i]]=i 
        else:
            return [map[ele],i]

ans = twoSum([2,7,11,15],9)
print(ans)