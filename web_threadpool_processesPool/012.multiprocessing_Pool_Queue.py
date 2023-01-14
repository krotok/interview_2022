from multiprocessing import Process,Pool
import time
import urllib2

def doubler(number):
    return number * 2


if __name__ == '__main__':
    pool = Pool(processes=12)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))