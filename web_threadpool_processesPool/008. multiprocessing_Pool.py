#To use the Pool class, we also have to create a separate function that takes a list item as an argument like we did
# when using Process. Then, using the multiprocessing module, create a Pool object called pool. This object has a function
# called map, which takes the function we want to multiprocess and the list as arguments and then iterates through the list
# for that function. After calling the function map, close the object to allow for a clean shutdown.

import time
import multiprocessing


def basic_func(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'


def multiprocessing_func(x):
    y = x * x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':
    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0, 199))
    pool.close()
    print('That took {} seconds'.format(time.time() - starttime))

