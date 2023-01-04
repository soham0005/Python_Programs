def palindromeNumber(num):
    # solution 1
    print(str(num)[::-1] == str(num))

    #Solution 2
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(reversed_num)
    return int(num) == int(reversed_num)

ans = palindromeNumber(121)
print(ans)
