#prints the permutation from the built-in function
from itertools import permutations
k = input("Enter  String and number:").split()
l = list(permutations(sorted(k[0]), int(k[1])))
for i in l:
    print("".join(i))
