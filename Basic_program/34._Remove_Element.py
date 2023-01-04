'''
Remove all the occurence of the element and return the length of new array/or how many times the number is popped.

'''
# def removeElement(num,val):
#     i,k = 0,0
#     while k<len(num):
#         if num[k] != val:
#             print(f'i value:{i}')
#             num[i] = num[k]
#             i+=1
#         print(f'k value before decrementing:{k}')
#         k+=1
#     return i


# Another Solution

def removeElement(num,val):
    while val in num:
        num.remove(val)
    return len(num)
ans = removeElement([0,1,2,2,3,0,4,2],2) 
print(ans)