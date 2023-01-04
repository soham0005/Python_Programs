def sumOfDigits(num):
    sumNum = 0
    for j in str(num):
        sumNum+= int(j)
    return sumNum
    
ans = sumOfDigits(12345)
print(ans)