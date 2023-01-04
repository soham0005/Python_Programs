'''
Higher Order Functions are the functions which takes another as parameters.
Ex: Map,Filter, Reduce.

Application for Map:
1) To Traverse on individual elements.
2) To perform some operation 

Application for Filter:
1) Select some Values based on criteria.

Application for Reduce:
NOTE: Reduce must be imported from functools
1) To perform some operation and return single value.

'''

'''
Filter:
takes 2 arguement (function,iterator)

'''
from functools import reduce

list1 = [1,2,3,4,5,6,7,8,9,10]

# Fetch Even Values from List.
evenList = list(filter(lambda ele:ele % 2 == 0,list1))
print(evenList)

# multiply all the values by 3 of even list.
MulBy3 = list(map(lambda ele: ele * 3,evenList))
print(MulBy3)

# Sum all the Values
sumVal = reduce(lambda a,b: a+b,MulBy3)
print(sumVal)