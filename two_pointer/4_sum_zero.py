'''
Problem Statement:- Find pairs that sums exactly to zero.
Criteria:- Array must be sorted.
'''

def sum_zero(arr):
    pair = []
    start = 0
    end = len(arr) - 1

    while(start < end):
        if(arr[start]+arr[end] == 0):
            pair.append([arr[start],arr[end]])
            start = start + 1
            end = end - 1
        elif(arr[start] + arr[end] > 0):
            end = end - 1
        else:
            start = start + 1
    return pair

ans = sum_zero([-3,-2,-1,0,1,2,4])
print(ans)
