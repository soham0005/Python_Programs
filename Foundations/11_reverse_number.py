def ReverseNum(num):
    num = str(num)
    reverseNum = list(num)
    reverseNum.reverse()
    print(int(''.join(reverseNum)))


ReverseNum(2000111)