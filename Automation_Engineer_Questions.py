# анаграмма O(n log n)
#
def is_anagram(s, t):
    return sorted(s) == sorted(t)


# быстрая реализация поиска анаграм O(n)
def is_anagram_quick(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)


a = 'ampo'
b = 'apom'
print(is_anagram(a, b))
print(is_anagram_quick(a, b))

# какие буквы присутствут несколько раз
a = ['a', 'b', 'c', 'b', 'a', 'a']
b = 'abcbaa'


def find_duplicates(nums):
    return list(set([x for x in nums if nums.count(x) > 1]))


print(find_duplicates(a))
print(find_duplicates(b))


# Удаление дубликатов из списка O(n)
def remove_duplicates(lst):
    return list(set(lst))


# полиндром O(n)
a = ['a', 'b', 'c', 'b', 'a']
b = 'abcba'
c = 'python best practices'

if b == b[::-1]:
    print("Polyndrom")

# Количество букв а
print('Mary had a little lamb'.count('a'))

# количество каждого символа в строке
from collections import Counter
def count_chars(s):
    return Counter(s)


print(count_chars(a))
print(count_chars(b))
print(count_chars(c))

# Количество одинаковых слов в строке
from collections import Counter
def word_count(s):
    return Counter(s.split())


s = "momo dodo momo momo dodo"
print(word_count(s))

# Количество слов в строке
print(len(s.split()))


# Поиск второго наибольшего числа O(n log n)
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]


l = [10, 8, 8, 9, 12]
print(second_largest(l))


# сумма всех цифр числа
def digit_sum(n):
    return sum(int(x) for x in str(abs(n)))


print(f"Sum : {digit_sum(12345)}")

print(f"Prime {10 ** 0.5}")


# является ли число простым O(√n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(f"Is prime: {is_prime(571)}")
# является ли число простым. вариант 2
def prime_num(num):
    max_div = int(num ** 0.5)
    for div_num in range(2, max_div+1):
        if num % div_num == 0:
            return False
    return True

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    print(f"{item} is prime") if prime_num(item) else None
    #print(f"{item}: {prime_num(item)}")

# Factorial  O(n)
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


m = 5
print(f"Factorial {m} is {factorial(m)}")


# Удалиtь N-ый элемент
def remove_element(lst, n):
    index = len(lst) - n
    return lst[:index] + lst[index + 1:]

from typing import List
def remove_element_del(my_string : str,n: int) -> str :
    index = n - 1
    my_lst = list(my_string)
    print(f"my_list:{my_lst.pop(index)}")
    print(my_lst)
    return "".join(my_lst)

print(remove_element("12345", 3))
print(remove_element_del("12345", 3))
# Генерация всех перестановок O(n!)
from itertools import permutations


def all_permutations(s):
    return list(permutations(s))


print(all_permutations("123456"))


# Перемножение двух матриц O(n³)
def multiply_matrices(a, b):
    result = [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
    return result


print(f"{17 / 4}")
print(f"{17 // 4}")
print(f"{round(-17 / 4, 2)}")
print(f"{-17 // 4}")

# Отсортировать буквы по частоте повторения O(n log n)
from collections import Counter


def sort_by_freq(nums):
    return sorted(nums, key=lambda x: (-Counter(nums)[x], x))


s = "ttyyhujjhtg"
print(f"frequency sort:{sort_by_freq(s)}")


# лямбда 1
def my_filter(a, filter=None):
    if filter is None:
        return a
    res = []
    for i in a:
        if filter(i):
            res.append(i)
    return res


lst = [1, 2, 3, 4, 5, 6, 7]
print(my_filter(lst, lambda x: x % 2 == 0))

# map
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x * 2, current_list))
print(new_list)

# filter
some_list = [1, 2, 3, True, 4.5]
print(list(filter(lambda x: isinstance(x, int), some_list)))

# zip()
# .sort and sorted() and sorted(key=)
# Отсортировать

# Отсортировать по ключу
# Вывести сначала упорядочные чётные , а потом нечётные. Присваиваем приоритет каждомы елементу
a = [12, -11, 102, -35, 35, -12]
def my_sort(x):
    return x if x % 2 == 0 else x + 1000

print(f'my_sort:{sorted(a, key=my_sort)}')

my_lst = (
    ("Semionov", "santehnik", 100),
    ("Petrov1111", "santehnik", 200),
    ("Ivanov", "manager", 300)
)
# Отсортировать по первой букве фамилии
print(sorted(my_lst, key=lambda x: x[0][0]))
# Отсортировать по зарплате
print(sorted(my_lst, key=lambda x: x[2]))
# Отсортировать по длинне фамилии
print(sorted(my_lst, key=lambda x: len(x[0])))

# all() and any()

ttt = [1,2,3,4,5,6]
print(ttt[1:])
print(ttt[2:])
print(ttt[:1])
print(ttt[:2])
print(ttt[:-1])
print(ttt[:-2])
print(ttt[:])
print(ttt[:])
print(ttt[::-1])
print(ttt[::2])

P = ['x','x','x','x','o','o','x','o','o']

def check_x(x):
    return all(map(lambda i: i == 'x',x))

#сумма цифр в числе
n = 123
#for char in str(n):
print(sum( int(x) for x in str(n)))

#число Армстронга
for number in range(100,1000):
    current_sum = sum(int(x)**3 for x in str(number))
    #print(type(current_sum), current_sum)
    if current_sum == number:
        print(f"Armstrong:{number}")

from collections import Counter


def find_max_char_occurrence(input_string: str) -> dict:
    """
    Finds the character(s) with the highest occurrence in a string.

    Args:
        input_string: The string to analyze.

    Returns:
        A dictionary containing the most frequent character(s) and their count.
        Returns an empty dictionary if the input string is empty.
    """
    if not input_string:
        return {}

    char_counts = Counter(input_string)
    max_count = max(char_counts.values())

    return {char: count for char, count in char_counts.items() if count == max_count}

my_string = "aaabbbbcccc"
print(f"Max occurrence: {find_max_char_occurrence(my_string)}")