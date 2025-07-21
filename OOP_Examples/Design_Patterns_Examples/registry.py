#Registry pattern применяется когда нужно хранить ссылки на все экземпляры класса

class A:
    registry = []

    def __init__(self, name):
        self.name = name
        A.registry.append(self)

a1 = A("first")
a2 = A("second")
a3 = A("third")

print([obj.name for obj in A.registry])  # ['first', 'second', 'third']
