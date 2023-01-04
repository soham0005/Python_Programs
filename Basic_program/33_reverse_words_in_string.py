#Example:  sky is blue 
#Output:    blue is sky

def reverseWord(s):
    s=' '.join(s.split()).split(" ")
    s.reverse()
    return ' '.join(s)

ans = reverseWord("a good   example")
print(ans)