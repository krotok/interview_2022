from multiprocessing import Semaphore

import requests
import concurrent.futures

input_urls = {
    #"url1":"http://51.105.241.115/interview_app_1/",
    #"url2":"http://51.105.241.115/interview_app_2/",
    #"url3":"http://51.105.241.115/interview_app_1/sample?test=4000",
    #"url4":"http://51.105.241.115/interview_app_2/sample?test=4000",
    "url5":"http://www.facebook.com",
    "url6":"http://www.google.com",
    "url7":"http://www.walla.com"
}


# SuperFastPython.com
# example of bounding the number of tasks submitted to the thread pool
from time import sleep
from time import time
from random import random
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor


# mock task that sleeps for a moment
def work(identifier, url):
    sleep(random())
    send_request(page_url=url, timeout=100)
    return identifier


# callback for completed tasks
def task_complete_callback(future):
    global semaphore
    # release the semaphore
    semaphore.release()


# proxy for submitting tasks that imposes a limit on the queue size
def submit_proxy(function, *args, **kwargs):
    global semaphore, executor
    # acquire the semaphore, blocks if occupied
    semaphore.acquire()
    # submit the task normally
    future = executor.submit(function, *args, **kwargs)
    # add the custom done callback
    future.add_done_callback(task_complete_callback)
    return future

def send_request(page_url, timeout=10):
    response = requests.get(url=page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    print(page_url + " - " + page_status + " " + str(response.elapsed.total_seconds()) + " " + str(sum(len(chunk) for chunk in response.iter_content(8196))))

# number of works in the pool
n_workers = 2
# max number of queued tasks
n_queue = 10
# semaphore to limit the queue size to the pool
semaphore = Semaphore(n_queue)
with ThreadPoolExecutor(n_workers) as executor:
    # submit many tasks
    futures = [submit_proxy(work, url_name, url_address) for url_name, url_address in input_urls.items()]
    # wait for all tasks to complete
    print('All tasks are submitted, waiting...')