array1 = [5,4,3,2,1,0]
# array.reverse() modifies theoriginal string
def reverse_1(arr):
    arr.reverse()
    print(arr)


#using swapping
def reverse_2(array):
    start = 0
    end = len(array)-1

    while(start<=end):
        (array[start],array[end])=(array[end],array[start])
        start+=1
        end-=1
    print(array)



#using reversed() method

def reverse_3(array):
    rev = list(reversed(array))
    print(rev)


# using list slicing
def reverse_4(array):
    print(array[::-1])


# reverse_1(array1)
# reverse_2(array1)
reverse_3(array1)
reverse_4(array1)