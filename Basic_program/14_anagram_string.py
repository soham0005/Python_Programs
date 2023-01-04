# If two string has same letter and same length then the two strings are anagrams

# Logic :- Split all the string , sort them and join those string and return their comparison.



# split string into letters---> list(str1)

# sort the string 
# ''.join(sorted(str1))
str1 = "soham"
str2 = "soham1"

str1 =  ''.join(sorted(str1))
str2 = ''.join(sorted(str2))
print(str1 == str2)