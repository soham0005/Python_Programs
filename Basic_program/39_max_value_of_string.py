def max_value(strs):
    maxLen = -1
    for ele in strs:
        if ele.isdigit():
            maxLen = max(maxLen,int(ele))
        else:
            maxLen = max(maxLen,len(ele))
    return maxLen

ans = max_value(["1","01","001","0001"])
print(ans)