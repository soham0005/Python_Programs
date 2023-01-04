from collections import Counter


def minRoundsToComplete(tasks):
    dic = Counter(tasks)
    count = 0

    for i in dic:
        n = dic[i]
        if dic[i] == 1:
            return -1

        elif n%3 ==0:
            count +=n//3
        
        else:
            k = n%3
            count += n//3+1
    return count



ans = minRoundsToComplete([2,2,3,3,2,4,4,4,4,4])
print(ans)