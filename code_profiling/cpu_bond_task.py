# cpu_bound_example.py

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    count = 0
    for i in range(limit):
        if is_prime(i):
            count += 1
    return count

if __name__ == "__main__":
    print(count_primes(10000000))
