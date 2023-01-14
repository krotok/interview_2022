# Abstract classes
from abc import ABC, ABCMeta, abstractmethod


class A(ABC):
    @abstractmethod
    def some(self):
        pass


class B(A):
    def some(self):
        pass


# Metaclasses

class C(ABCMeta):
    @abstractmethod
    def some(self):
        pass
#Generators  #############################

a = (i**2 for i in range(1,5))
print(a)
print(next(a))
print(next(a))
print(next(a))

## Generators ----------------------------
def f_gen(m):
    s = 1
    for n in range(2, m):
        yield n ** 2 + s
        s += 1

a = f_gen(5)
print(a)

for i in a:
    print("Continue numbering")
    print(i)

