def ValidParanthesis(string):
    d = {"(":")","{":"}","[":"]"}
    stack = [] 
    for i in string:
        if i in d:
            stack.append(i)
        elif len(stack) ==0 or d[stack.pop()]!=i: 
           return False

    return len(stack) == 0


result = ValidParanthesis("()[]{}")
print(result)