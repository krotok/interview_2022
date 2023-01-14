from time import sleep
from concurrent.futures.thread import ThreadPoolExecutor
from random import random


def task(name):
    # sleep for less than a second
    i = 0
    while i < 10:
        i = random() * 100
    print(f"sleep {i}")
    sleep(i)
    return f'Task: {name} done.'

def task2(name):
    # sleep for less than a second
    i = 0
    while i < 10:
        i = random() * 100
    print(f"sleep {i}")
    sleep(i)
    print(f'Task: {name} done.')

# # start the thread pool
# with ThreadPoolExecutor(10) as executor:
#     # execute tasks concurrently and process results in order
#     for result in executor.map(task, range(10)):
#         # report the result
#         print(result)

# start the thread pool
# with ThreadPoolExecutor(10) as executor:
#     # handle a timeout error when getting results
#     try:
#         # iterate the results from map performed in separate threads, wait a limited time
#         for result in executor.map(task, range(10), timeout=0.05):
#             print(result)
#     except TimeoutError:
#         print('Waited too long')

# start the thread pool
with ThreadPoolExecutor() as executor:
    # submit all tasks
    executor.map(task2, range(5))
    # shutdown, wait for all tasks to complete
    print("Waiting .... ")
print('All done.')



