def LinearSearch(arr,target):
    for ele in arr:
        if ele == target:
            return True
    return False

ans = LinearSearch([1,2,3,4,5,5,6,3,2],10)
print(ans)
