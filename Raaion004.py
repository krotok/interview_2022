#18 custing
date_as_string = '20-05-1994'
day, month, year = map(int, date_as_string.split('-'))
print(type(day))
print(type(month))
print(type(year))

#19 видимость атрибутов классов  ###############
class A():
    some_method =   1
    _some_method =  2
    __some_method = 3

class B(A):
    pass

a=A()
print(a.some_method)
print(a._some_method)
print(a._A__some_method)

b=B()
print(b.some_method)
print(b._some_method)
print(b._A__some_method)

