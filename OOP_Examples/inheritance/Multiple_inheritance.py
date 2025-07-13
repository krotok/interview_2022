#Multiple Inheritance
class Parent1:
    def __init__(self):
        print("Конструктор Parent1")

class Parent2:
    def __init__(self):
        print("Конструктор Parent2")

class Parent3:
    def __init__(self):
        print("Конструктор Parent3")

class Child_MRO(Parent1, Parent2, Parent3):
    def __init__(self):
        super().__init__()  # Вызывает только Parent1 из-за MRO
        print("Конструктор Child")

class Child_MRO_Manual(Parent1, Parent2, Parent3):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        Parent3.__init__(self)
        print("Конструктор Child")


if __name__ == "__main__":
    print("---Child_Manual---")
    obj1 = Child_MRO()
    print(Child_MRO.mro())

    print("---Child_MRO_Manual---")
    obj2 = Child_MRO_Manual()
    print(Child_MRO_Manual.mro())