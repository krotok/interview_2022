#From:https://urban-institute.medium.com/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba#:~:text=Python's%20built%2Din%20multiprocessing%20module,multiple%20processors%20for%20simultaneous%20execution.

#The multiprocessing Python module contains two classes capable of handling tasks. The Process class sends each task to
# a different processor, and the Pool class sends sets of tasks to different processors. We will show how to multiprocess
# the example code using both classes. Although both classes provide a similar speed increase, the Process class is more
# efficient in this case because there are not many processes to execute. Pool is most useful for large amounts of processes
# where each process can execute quickly, while Process is most useful for a small number of processes where each process
# would take a longer time to execute.

#To use the Process class, place the functions and calculations that are done on each list item in its own function that
# will take a list item as one of its arguments. Next, import the multiprocessing module, create a new process for each list
# item, and trigger each process in one call. We keep track of these processes by making a list and adding each process to it.
# After creating all the processes, take the separate output of each CPU and join them into a single list.

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
    processes = []
    for i in range(0, 1000):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('That took {} seconds'.format(time.time() - starttime))

