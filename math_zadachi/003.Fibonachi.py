#Computing the value of a Fibonacci number can be implemented using recursion. Given an input of index N, the recursive function has two base cases – when the index is zero or 1. The recursive function returns the sum of the index minus 1 and the index minus 2.
#The Big-O runtime of the Fibonacci function is O(2^N).

import time

#Recursion Fibonacci
def fibonacci_recursion(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


#Iterative Fibonacci
def fibonacci_iteration(n):
  if n < 0:
    raise ValueError("Input 0 or greater only!")
  fiblist = [0, 1]
  for i in range(2,n+1):
    fiblist.append(fiblist[i-1] + fiblist[i-2])
  return fiblist[n]

number = 35
start_time = time.time()
fibonacci_recursion(number)
end_time = time.time()
print(f"Calculating of fibonacci recursive {number} took {end_time - start_time} seconds ")

start_time = time.time()
fibonacci_iteration(number)
end_time = time.time()
print(f"Calculating of fibonacci iteration {number} took {end_time - start_time} seconds ")