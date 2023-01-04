def gcd(num1,num2):
    if(num2!=0):
        return gcd(num2,num1%num2)
    else:
        return num1

result = gcd(366,60)
print(result)