import math
def square_root(num):
    start = 0
    end = num
    ans= -1

    while(start<=end):
        mid = math.floor(start + (end-start)/2)
        
        if(mid*mid == num):
            return mid
        elif(mid*mid > num):
            end = mid-1 
        else:
            ans = mid
            start = mid+1

    return ans

ans = square_root(26)
print(ans)