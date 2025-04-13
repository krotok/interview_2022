#анаграмма O(n log n)
#



def is_anagram(s, t):
    return sorted(s) == sorted(t)
#быстрая реализация поиска анаграм O(n)
def is_anagram_quick(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)

a = 'ampo'
b = 'apom'
print(is_anagram(a,b))
print(is_anagram_quick(a,b))

#какие буквы присутствут несколько раз
a = ['a','b','c','b','a','a']
b = 'abcbaa'
def find_duplicates(nums):
    return list(set([x for x in nums if nums.count(x) > 1]))

print(find_duplicates(a))
print(find_duplicates(b))

# Удаление дубликатов из списка O(n)
def remove_duplicates(lst):
    return list(set(lst))


#полиндром O(n)
a = ['a','b','c','b','a']
b = 'abcba'

if b == b[::-1]:
    print("Polyndrom")

#Количество букв а
print('Mary had a little lamb'.count('a'))

#количество каждого символа в строке
from collections import Counter

def count_chars(s):
    return Counter(s)

print(count_chars(a))
print(count_chars(b))

#Количество одинаковых слов в строке
from collections import Counter

def word_count(s):
    return Counter(s.split())

s = "momo dodo momo momo dodo"
print(word_count(s))

#Количество слов в строке
print(len(s.split()))

# Поиск второго наибольшего числа O(n log n)
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

l = [10,8,8,9,12]
print(second_largest(l))

#сумма всех цифр числа
def digit_sum(n):
    return sum(int(x) for x in str(abs(n)))

print(f"Sum : {digit_sum(12345)}")

print(f"Prime {10**0.5}")

#является ли число простым O(√n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"Is prime: {is_prime(571)}")

#Factorial  O(n)
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

m = 5
print(f"Factorial {m} is {factorial(m)}")

#Удалиtь N-ый элемент
def remove_element(lst,n):
    index = len(lst) - n
    return lst[:index] + lst[index+1:]

print(remove_element("12345", 3))

#Генерация всех перестановок O(n!)
from itertools import permutations

def all_permutations(s):
    return list(permutations(s))
print(all_permutations("123456"))

#Перемножение двух матриц O(n³)
def multiply_matrices(a, b):
    result = [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
    return result

print(f"{17/4}")
print(f"{17//4}")
print(f"{-17/4}")
print(f"{-17//4}")

