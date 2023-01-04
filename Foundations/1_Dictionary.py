# Creation of Dictionary:-

dict = {}
# dict = dict()

# Accessing Dictionary/Adding
dict["Soham"] = "Adhyapak"
dict.update({"Hobbies":["Valorant","Horror Movies"]})
dict['Age'] = 19
print(dict)

# Deleting Element From Dictionary
del dict['Age']
dict.pop("Age")

print(dict)

# pop(key)--> removes specified pair.

#popitem()---> Removes last pair


# Check if pair exist in dictionary 
'''
1) Using if in pair
2) Using try-except
'''

dictionary1 ={"1":10,2:20,3:30,4:40}

if 1 in dictionary1:
    print(dictionary1[1])

# Loop in dictionary

for key in dictionary1:
    print(dictionary1[key])

# Alternate way

for key in dictionary1.keys():

    print(key)


# print key and value using loop

for key,value in dictionary1.items():
    print(key,":",value)