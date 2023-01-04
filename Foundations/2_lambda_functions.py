'''
One Liner Functions/Anonymous Functions
Can Have Multiple arguements but only one expression.

Lambda Keyword is used.
Anything after lambda and before ":" is treated as parameters.

Default Values can also be added in lambda function.
Ex:

'''

# Example 1 For addition of numbers.
def add(num1,num2):
    print(num1+num2)

# Lambda function for add function

add = lambda a,b:print(a+b)

add(10,30)

# without function name[IIFE]
# Syntax:- (lambda:a,b:10*20)(10,10)

(lambda a,b:print("Mulitplication: ",a*b))(10,30)
