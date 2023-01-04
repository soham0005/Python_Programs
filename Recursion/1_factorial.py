def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num - 1)

ans = factorial(5)
print(ans)