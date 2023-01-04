def validParanthesis(string):
    stack = []
    data = {"(":")","{":"}","[":"]"}

    for i in string:
        if i in data:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0
     

