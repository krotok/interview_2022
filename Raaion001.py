my_dict001 = {}.fromkeys('ABC', 'ZTY')
print(f"My dict: {my_dict001}")
for name,value in my_dict001.items():
    print('the name of the  dictionary element is ', name)
    print('the element value ', value)
print(f"Keys {my_dict001.keys()}")
#######################
myset = set()
print(type(myset))
#######################
def some_finc(some_list: list = []):
    some_list.append(1)
    return some_list

print(some_finc())
print(some_finc())
print(some_finc())
print(some_finc())
print(some_finc([2]))
print(some_finc())

