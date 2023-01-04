def printPrime(m,n):
    # prime = []
    # for i in range(m,n):
    #     if i ==0 or i == 1:
    #         continue
    #     else:
    #         for j in range(2,int(i/2)+1):
    #             if i%j == 0:
    #                 break
    #             else:
    #                 prime.append(i)
    # return prime
    prime_list = []
    for i in range(m, n):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

ans = printPrime(2,10)
print(ans)