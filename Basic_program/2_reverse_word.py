string = "Soham"

# using slicing.
print(string[::-1])


# using join and reversed().  
print("".join(reversed(string))) 



# using loop

str1 =""
for c in string: 
    str1 = c + str1

print(str1)