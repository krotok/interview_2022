class Test:
    def __init_subclass__(cls, /, test_param, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.test_param = test_param

class AnotherTest(Test, test_param="Hello World"):
    pass

#---------------------------

class Test:
    def __repr__(self):
        return "Hello World"

print(Test())
#--------------------

class Test:
    def __str__(self):
        return "Hello World"


test = Test()
print(str(test))


#21 ################
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def func1():
    pass

#----------------------
def my_decorator_2(func):
    def wrapper(*args, **kwargs):
        result = f'{func(*args, **kwargs)}!!!'
        return result
    return wrapper

@my_decorator_2
def add(a, b):
    '''Add two objects together, the long way'''
    return a + b

@my_decorator_2
def mysum(*args):
    '''Sum any numbers together, the long way'''
    total = 0
    for one_item in args:
        total += one_item
    return total


print(add(10, 20))
print(mysum(10, 20, 30, 40, 50))