class Grandparent:
    def __init__(self):
        print("Конструктор Grandparent")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Конструктор Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Конструктор Child")

obj = Child()
