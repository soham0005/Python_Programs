def two_sum(num, target):
    map = {}
    length = len(num)
    i=0

    while i<length:
        val = target - num[i]
        if val in map:
            return [map[val],i]
        map[num[i]]=i
        i += 1

ans = two_sum([2,7,11,15],9)
print(ans)