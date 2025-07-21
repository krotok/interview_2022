#Создать валидацию координат вектора с помощю внутри класса  @classmethod
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls,arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

        # можно так сделать условие  через имя класса
        #if Vector.validate(x) and Vector.validate(y):
        # но с self это более универсально, если имя класса изменится. В этом случае интерпритатор поймёт с каким классом раборать
        #и вместо cls в методе validate подставит класс Vector
        if self.validate(x) and self.validate(y):                                                          #
            self.x = x
            self.y = y

    def get_coordinates(self):
        return (self.x , self.y)

v = Vector(10,20)
print(f"Vector: {v.get_coordinates()}")
print(f"Vector: {Vector.get_coordinates(v)}")

p = Vector(200,300)
print(f"Vector: {p.get_coordinates()}")
#######################################################
class A(object):
    def foo1(self):  # Обычный метод, первым параметром должен быть self, который представляет сам конкретный экземпляр.
        print('Hellow', self)

    @staticmethod
    def foo2():  # Если вы используете staticmethod, вы можете игнорировать это self и использовать этот метод как обычную функцию.
        print('hello')


    @classmethod
    def foo3(cls):  # Для метода class его первый параметр не self, а cls, который представляет сам класс.
        print('hellow', cls)

if __name__ == "__main__":
    a = A()
    a.foo1()  # Hellow <__ main __. Объект по адресу 0x102a08908> (указывающий, что это экземпляр класса)
    A.foo2()  # hello (бесполезно)
    A.foo3()  # hellow <class '__ main __. A'> (указывая, что это класс)

###########################################
#использование classmethod  с глобальной переменнои

class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)


# Создаем объекты родительского класса
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
# Вызываем classmethod
MyClass.total_objects()
print(MyClass.TOTAL_OBJECTS) #можно распечатать и так. Зачем же этот  @classmethod???

# Создаем дочерний класс
class ChildClass(MyClass):
    TOTAL_OBJECTS=0
    pass
ChildClass.total_objects()


###########################################################

#Использование classmethod как конструктор класса
#так можно создавать многие конструкторы принимающие различные значения
class DateTime(object):

    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, string_date):
        day, month, year = map(int, string_date.split('-'))
        myDate = cls(day, month, year)
        return myDate

    @staticmethod
    def is_valid_date(date_as_string):
        #upnpacking  стринга с custing в int
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

dateObj = DateTime.from_string('20-05-1994')
date_attributes = dir(dateObj)
print(f"date_attributes: {date_attributes}")

print(f"dateObj:{dateObj.__dir__()}")

#2 ways to get all fields with values
print(f"All fields:{vars(dateObj)}")
import pprint
pprint.pprint(f"All fields pprint:{vars(dateObj)}")

is_valid_date = DateTime.is_valid_date('20-05-1994')
print(f"is_valid_date:{is_valid_date}")

################################################
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()