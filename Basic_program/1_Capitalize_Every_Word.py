import string as st
# Method 1 using module.
string = "chris alan" 
print(st.capwords(string))  

# Method 2 using Loop
cap_string = ""
for ele in string: 
    cap_string = cap_string + ele.capitalize()
print(cap_string)

# Method 3 using title()
print(string.title())
