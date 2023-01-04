def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

ans = int(input("Enter the Number:"))
for i in range(0,ans):
    print(fib(i))