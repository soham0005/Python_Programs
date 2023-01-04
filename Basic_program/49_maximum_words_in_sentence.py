def maxWordsFound(sentences):
    result = 0
    for i in sentences:
        result = max(result,i.count(' '))
    return result+1

ans = maxWordsFound(["please wait","continue to fight","continue to win"])
print(ans)
