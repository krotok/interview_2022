import multiprocessing
import requests
import time

flag = True
start_time = time.time()

urls = [
    'http://www.facebook.com',
    'http://www.google.com',
    'http://www.cnn.com',
    'http://www.facebook.com',
    'http://www.google.com',
    'http://www.cnn.com',
    'http://www.facebook.com',
    'http://www.google.com',
    'http://www.cnn.com',
    'http://www.facebook.com',
    'http://www.google.com',
    'http://www.cnn.com'
]

def fetch(url):

    while True:
        response = requests.get(url)
        print(multiprocessing.current_process().name)
        return multiprocessing.current_process().name, response.status_code


if __name__ == '__main__':

    while flag:
        with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
            results = p.map(fetch, urls)

        for url, status in results:
            print(url, status)
        # if time.time() - start_time > 10:
        flag = False

        p.close()
        p.join()
