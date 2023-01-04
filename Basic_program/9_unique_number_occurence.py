'''
Problem Statement: Return True if all the occurence of all elements are unique.
'''

def unique_occ(arr):
    obj ={}
    for ele in arr:
        if ele in obj:
            obj[ele]+=1
        else:
            obj[ele] = 1
    occValues = obj.values()
    setValues = set(occValues)
    print(len(occValues) == len(setValues))
        

    

unique_occ([1,2,2,1,1,3])
