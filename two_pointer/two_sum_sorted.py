'''
Problem Statement:- Two Sum for sorted array, only one distinctranswer is possible
'''


def two_sum(arr,target):
    start = 0 
    end = len(arr) - 1
    ans = []
    while(start < end):
        if((arr[start]+arr[end])==target):
            ans.append([arr[start],arr[end]])
            start+=1
            end-=1
        elif((arr[start]+arr[end])>target):
            end-=1
        else:
            start+=1
    return ans

ans = two_sum([1,2,3,4,6],4)
print(ans)

