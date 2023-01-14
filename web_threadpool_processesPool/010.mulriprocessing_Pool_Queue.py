import time
from multiprocessing import Process, Queue


def writer(i, q):
    message = f'I am Process {i}'
    q.put(message)


if __name__ == '__main__':
    # Create multiprocessing queue
    q = Queue()

    # Create a group of parallel writers and start them
    for i in range(10):
        Process(target=writer, args=(i, q,)).start()
    # Read the queue sequentially
    #for i in range(10):
    flag = True
    start_time = time.time()
    test_duration = 2
    while (flag == True):
        message = q.get()
        print(message)
        print(time.time() - start_time)
        if time.time() - start_time > test_duration:
            flag == False