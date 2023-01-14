import math

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if(num % i == 0):
            return False
        # no divider in the mathematical range of [2, sqrt]
    return True

def print_is_prime(num: int) -> None:
    print(num, "is", "\b" if is_prime(num) else "not", "a prime")

def print_is_prime_upto(num: int) -> None:
    for i in range(1, num + 1):
        print_is_prime(i)


print_is_prime_upto(675)

# Exesize



def print_any_args_number(*args, end_line : str = "\n", separator: str = " "):
    for item in (args):
        print(item,separator)

    print(end_line)
    print('tttt\nPython is included in CodeSpeedy\r123456789')

print_any_args_number("123",123,"234", 234)