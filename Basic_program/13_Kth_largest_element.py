def findKthElement(arr,k):
    arr.sort()
    return arr[len(arr)-k]

ans = findKthElement( [3,2,1,5,6,4],2)
print(ans)