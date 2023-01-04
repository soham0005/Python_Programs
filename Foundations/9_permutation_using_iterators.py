import itertools   

a_list=[1, 2, 3]

perm = [list(x) for i in range(1, len(a_list)+1) for x in itertools.permutations(a_list, i)]