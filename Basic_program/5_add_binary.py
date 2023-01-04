def add_binary(a,b):
   return bin(eval('0b' + a) + eval('0b'+ b))[2:]
    

res = add_binary("11","1")
print(res)
