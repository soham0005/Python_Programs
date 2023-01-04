def swapCase(s):
    swap = ''
    
    for i in s:
        if i.isupper():
            i = i.lower()
            swap += i
        elif i.islower():
            i = i.upper()
            swap += i
        else:
            swap += i
    return swap

ans = swapCase('HackerRank.com presents "Pythonist 2".')
print(ans)