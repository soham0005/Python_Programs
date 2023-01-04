sample_list = [1,2,3,4,5,6,7]

# Squaring all numbers using list comprehension
# ALternative for map


# Overall Syntax:-
# [variable*(operation if any) for variable in list ((if conditon) if any )]
doubles = [n**2 for n in sample_list]
print(doubles)


sample_data = [5, -1, -2, 0, 3]

negatives = [n for n in sample_data if n<0 ]
print(negatives)