def pairSum(arr,s):
    size=len(arr)
    ans=[]

    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]+arr[j]==s:
                temp=[]
                temp.append(min(arr[i],arr[j]))
                temp.append(max(arr[i],arr[j]))
                ans.append(temp)
    return sorted(ans)

ans = pairSum([1,2,3,4,5],5)
print(ans)
