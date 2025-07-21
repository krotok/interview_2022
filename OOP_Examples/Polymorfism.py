#Полиморфизм в методах
def add(a, b):
    return a + b

print(add(1, 2))  # 3
print(add("Hello, ", "World"))  # Hello, World

#Полиморфизм без наследования
class Rectangle:
    def area(self):
        return 10 * 5

class Circle:
    def area(self):
        return 3.14 * 5 * 5

shapes = [Rectangle(), Circle()]
for shape in shapes:
    print(shape.area())

#Использование полиморфизма с функциями-обработчиками
class Button:
    def click(self):
        print("Button clicked")

class Link:
    def click(self):
        print("Link clicked")

def handle_click(element):
    element.click()

button = Button()
link = Link()
handle_click(button)  # Button clicked
handle_click(link)  # Link clicked


#Полиморфизм в классах с наследоваием
class A:
    def __init__(self):
        self.var = "Class A var 1"
        self.var2 = "Class A var2"

    def sound(self):
        return (self.var,self.var2)

class B(A):
    def __init__(self):
        super().__init__()
        self.var = "Class B"

    def sound(self):
        return self.var

class C(A):
    def __init__(self):
        super().__init__()
        self.var = "Class C"

    def sound(self):
        return self.var

class D(B,C):
    def __init__(self):
        super().__init__()
        self.var = "Class D"

    def sound(self):
        return self.var

mylist = [A(), B(), C(), D()]

#полиморфизм
for x in mylist:
    print(x.sound())

#наследование
d = D()
print(d.var2)

#########################################################
class Transport:
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Deliver by land")

class Ship(Transport):
    def deliver(self):
        print("Deliver by sea")

# Полиморфизм в действии
def make_delivery(transport: Transport):
    transport.deliver()

make_delivery(Truck())  # Deliver by land
make_delivery(Ship())   # Deliver by sea
#########################################################