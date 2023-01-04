def Kth_Smallest(arr,k):
    arr.sort()
    return arr[k-1]

ans = Kth_Smallest([7,4,3,10,20,14],3)
print(ans)