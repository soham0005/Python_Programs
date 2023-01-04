string=input()
obj={}
for ele in string:
    if ele in obj:
        obj[ele]+=1
    else:
        obj[ele]=1
if 2*obj['z']==obj['o']:
    print("Yes")
else:
    print("No")
