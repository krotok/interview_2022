class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

######################################################3
#Abstract Classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    @classmethod
    def sound(self):
        return "Myau!!!"

#############################Metaclasses
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_method'] = lambda self: "New method added by metaclass"
        return super().__new__(cls, name, bases, dct)

class MyClass2(metaclass=MyMeta):
    pass

#Dynamic classes
MyClass3 = type('MyClass3', (object,), {'x': 5})

#Static classes
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


if __name__=="__main__":
    mc = MyClass("Vasia")
    print(mc.greet())


    my_dog = Dog()
    print(my_dog.sound())
    my_cat = Cat()
    print(my_cat.sound())

    my_animals : [Animal] = (my_dog,my_cat)
    for pat in my_animals:
        print(pat.sound())

    obj = MyClass2()
    print(obj.added_method())  # Выведет: New method added by metaclass


    obj = MyClass3()
    print(obj.x)  # Выведет: 5

    print(MathUtils.add(3, 3))
    print(MathUtils.multiply(3,3))