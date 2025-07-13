class Parent:
    def __init__(self):
        print("Конструктор Parent")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Конструктор Child1")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Конструктор Child2")

obj1 = Child1()
obj2 = Child2()
