def unique(mydict):
    return list(mydict.keys())[list(mydict.values()).index(1)]


ans = unique({1:2,2:2,3:1,4:2,5:3})
print(ans)

# list constructor(for keys) 
# [list(mydict.values()).index(1)]