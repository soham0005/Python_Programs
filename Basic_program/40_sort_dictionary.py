def sort_dict(arr1,arr2):
    import operator
    dict = {}
    n = len(arr1)
    for i in range(n):
        dict[arr1[i]] = arr2[i]
    print(sorted(dict.keys(),reverse=True))

sort_dict(["Mary","John","Emma"],[180,165,170])