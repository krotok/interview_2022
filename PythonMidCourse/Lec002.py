from typing import Optional


def check_item(my_list: list = "", item: str = ""):
    if item in my_list:
        return True
    else:
        return False


def check_item_appearances(my_list: list = "", item_to_search: str = ""):
    count = 0
    for item in my_list:
        if item == item_to_search:
            count = count + 1
    return count


def print_check_item(my_list: list = "", item: str = ""):
    print(item, "\b" if check_item(my_list, item) else "not", "in the list")


def print_check_item_appearances(my_list: list = "", item: str = ""):
    print(item, "present", check_item_appearances(my_list, item), "times in the list")


# print_check_item(["111", "321", "123"], "1239")
print_check_item_appearances(["123", "111", "123", "123"], "123")

########### Exercise : find the first index of an item in a list
def first_item_position(search_item: str = "", my_list : list = []) -> Optional[int]:
    for index, item in enumerate(my_list):
        if item == search_item:
            return index

from typing import List
def appearances_in_list(look_for, lst: list) -> List[int]:
 indices = []
 for index, item in enumerate(lst):
    if item == look_for:
        indices.append(index)
 return indices

#Exercise: get all primes till a certain limit
# from typing import List
# def get_all_primes_upto(num: int) -> List[int] :
#     primes : List[int] = []
#     for i in range(num + 1):
#         if is_prime(i):
#         primes.append(i)
#     return primes

#Print List which hold itself
lst = [1,2,3]
lst.append(lst)
for item in lst:
    if type(item) == list:
        for item2 in item:
            print(f"'{item2}'", end='', sep='')
    elif type(item) == int:
        print(f"'{item}'", end='', sep='')
    else:
        print(item, end='')

# def my_print_list(lst, in_printing_of):
#     if in_printing_of is None:
#         in_printing_of = []
#     elif id(lst) in in_printing_of:
#         print("[...]", and=' ')

#Find min,max, avg
#Solution 1 with pandas
# import numpy as np
# import pandas
# s = pandas.Series(np.random.normal(size=100))
# stats = s.describe()  # stats is a dict with statistical data, e.g.: mean, std, min, max

#Solution 2
from typing import List, Tuple
def get_stats(lst: List[float]) -> Tuple[float] :
 count: int = len(lst)
 if count == 0: return None
 min : float = lst[0]
 max : float = lst[0]
 sum : float = 0
 for num in lst:
    if num < min: min = num
    elif num > max: max = num
    sum += num
 return min, max, sum/count