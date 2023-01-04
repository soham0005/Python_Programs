import math

def convertAndReverse(num):
    return str(abs(num))[::-1]


def reverseInteger(x):
    if x > math.pow(2,31) or x < -math.pow(2,31):
        return 0
    else:
        if x<0:
            x = convertAndReverse(x)
            return '-'+x

        else:
           x = convertAndReverse(x)
           return x
                  

ans = reverseInteger(-11123123)
print(ans)
