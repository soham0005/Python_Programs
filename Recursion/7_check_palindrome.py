def isPalindrome(str,i,j):
    if(i>j):
        return True
    
    if(str[i]!=str[j]):
        return False
    
    else:
        return isPalindrome(str,i+1,j-1)

string1 = "aaaa"
i=0
j = len(string1)-1
ans = isPalindrome(string1,i,j)
print(ans)