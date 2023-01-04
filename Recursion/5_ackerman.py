def ackerman(num1,num2):
    if(num1==0):
        return num2+1
    elif(num1>0 and num2==0):
        return ackerman(num1-1,num2)
    elif(num1>0 and num2 >0):
        return ackerman(num1-1,ackerman(num1,num2-1))

result = ackerman(0,5)
print(result)