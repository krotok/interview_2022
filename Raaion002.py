#######################
# lambda functions
some_list = [1, 2, 3, "h"]
print(list(filter(lambda x: isinstance(x, int), some_list)))
print(list(filter(lambda x: isinstance(x, str), some_list)))
#----------------------------------


my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)
##################################

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)

##################################
from functools import reduce
current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x + y), current_list)
print(summa)

##################################
tables = [lambda x = x: x*10 for x in range(1, 11)]
print(tables)
for x in tables:
    print(x())

##################################
max_number = lambda a, b: a if a > b else b
print(max_number(3, 5))

##################################
current_list = [[3,5,10,6,9],[16, 14, 1, 80],[8, 30, 29, 12, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
print(f"Sorted list {sorted_list}")
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)

##################################
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
for e in L:
    print(e.name)
print(list(item.name for item in L))
# вывод: ['David', 'Alex', 'Amanda']

##################################
def myFunc(e):
  return len(e)

cars1 = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars_lambda = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars1.sort(key=myFunc)
cars_lambda.sort(key=lambda x: len(x))
print(cars1)
print(cars_lambda)

##################################
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
##################################

some = True
result = 1 if some else 0
print(result)

################