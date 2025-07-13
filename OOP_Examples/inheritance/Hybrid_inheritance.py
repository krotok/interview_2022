#Several types of inheritance together
class Base:
    def __init__(self):
        print("Конструктор Base")

class Parent1(Base):
    def __init__(self):
        super().__init__()
        print("Конструктор Parent1")

class Parent2(Base):
    def __init__(self):
        super().__init__()
        print("Конструктор Parent2")

class Child_MRO(Parent1, Parent2):
    def __init__(self):
        super().__init__()  # MRO вызовет только Parent1
        print("Конструктор Child")

obj = Child_MRO()
print(Child_MRO.mro())
