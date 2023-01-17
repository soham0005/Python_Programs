# leet code questio flip string to monotone increasing.


def flipString(s):
    ones, ans = 0,0
    for ele in s:
        if ele == '1':
            ones+=1
        elif ones:
            ones-=1
            ans+=1
    return ans

ans = flipString("00110")
print(ans)