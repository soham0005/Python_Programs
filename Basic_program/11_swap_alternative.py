def swap_alternative(arr):
    for i in range(0,len(arr),2):
        if(i+1<len(arr)):
            (arr[i],arr[i+1]) = (arr[i+1],arr[i])

    return arr
 
ans = swap_alternative([2,1,4,3,6,5])
print(ans)