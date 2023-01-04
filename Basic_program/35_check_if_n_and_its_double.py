from collections import defaultdict
def checkN(arr):
    dict_number = defaultdict(int)
    for ele in range(len(arr)):
        if 2*arr[ele] in dict_number or arr[ele]/2 in dict_number:
            return True
        else:
            dict_number[arr[ele]] = ele
    return False

ans = checkN([3,1,7,11])
print(ans)