#Single
class Parent:
    def __init__(self, name):
        print(f"Родительский конструктор: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Вызываем конструктор родителя
        print(f"Дочерний конструктор: {age}")



if __name__ == "__main__":
    obj = Child("Иван", 10)

