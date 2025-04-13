import time

tumb = ["ножницы", "карандаш", "яблоко", "книга"]
print(iter(tumb[0]))
# получаем итератор для итерируемого объекта
it = iter(tumb)
print(it)
try:
    while True:
        next_val = next(it)
        print("Очередное значение:", next_val,",", it)
except StopIteration:
    # явно напечатаем сообщение об окончании итерации,
    # хотя цикл for этого не делает и ошибка просто подавляется
    print("Итерация закончена")
print("Программа завершена")

it = iter(tumb)
print(it)
try:
    while True:
        next_val = next(it)
        print("Очередное значение:", next_val,",", it)
except StopIteration:
    # явно напечатаем сообщение об окончании итерации,
    # хотя цикл for этого не делает и ошибка просто подавляется
    print("Итерация закончена")
print("Программа завершена")

# concatenate dict
boxes = {
            "one": ["1111","1222"],
            "two": ["2111","2222"],
            3: ["3111","3222"]
        }
boxes_items = boxes["one"] + boxes["two"] + boxes[3]
print(boxes_items)
print(",".join(boxes_items))

#Класс интератора который интерирует любые объекты
class MyIterable:
    def __init__(this,max):
        this.value = 0
        this.max = max
    def __iter__(this):
        return this
    def __next__(this):
        this.value += 1
        print("Current value", this.value)
        if this.value < this.max:
            return this.value
        else:
            raise StopIteration

l = [a for a in MyIterable(6)]
print(l)

###Классы для интерированиж объектов в тумбочке с 3мя ящиками
class TumbochkaIterator:
    def __init__(self,some_objects):
        self.some_objects = some_objects
        self.current = 0

    def to_start(self):
        self.current = 0

    def to_current(self, val):
        if val >= len(self.some_objects) or val < 0:
            print("Неверное значение для курсора!")
        else:
            self.current = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result
        raise StopIteration

class Tumbochka:
    def __init__(self):
        self.tumb_dict = {
        1 : [],
        2 : [],
        3 : [],
        }
    def add_to_tumb(self,box_number,item):
        self.tumb_dict[box_number].append(item)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        return  ",".join(self.tumb_dict[1] + self.tumb_dict[2] + self.tumb_dict[3])

    def __iter__(self):
        return TumbochkaIterator(self.tumb_dict[1] + self.tumb_dict[2] + self.tumb_dict[3]) #

tumb = Tumbochka()
tumb.add_to_tumb(1,"knighf")
tumb.add_to_tumb(2,"knighf")
tumb.add_to_tumb(3,"knighf")
tumb.add_to_tumb(1,"fock")
print(str(tumb))

for i in tumb:
    print(i,type(i),id(i))
    time.sleep(1)

# it= iter(tumb)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))