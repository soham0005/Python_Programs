def two_Sum(arr,k):
    map = {}
    l = len(arr)
    i = 0

    while i<l:
        val = k - arr[i]
        if val in map:
            return [map[val],i]
        else:
            map[arr[i]] = i
            i+=1

ans = two_Sum([2,7,11,15],9)
print(ans)
