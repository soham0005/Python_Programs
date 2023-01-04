def revKstring(s,k):
    s = [*s]
    start = 0
    end = k-1

    while(start<=end):
        s[start],s[end] = s[end],s[start]
        start+=1
        end-=1
    return ''.join(s)
ans = revKstring("abcde",3)
print(ans)
