class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_method'] = lambda self: "New method added by metaclass"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.added_method())  # Выведет: New method added by metaclass
