from multiprocessing import Semaphore

import requests
import concurrent.futures

raw_results = dict()
results = dict()

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

    #print(page_url + " - " + page_status + " " + str(response.elapsed.total_seconds()) + " " + str(sum(len(chunk) for chunk in response.iter_content(8196))))
    site_name = get_url_sitename(page_url)
    if site_name in raw_results:
        raw_results[site_name]["req_number"] = raw_results.get(site_name).get("req_number") + 1
        raw_results.get(site_name).get("response_time").append(response.elapsed.total_seconds())
        raw_results.get(site_name).get("throughput").append(sum(len(chunk) for chunk in response.iter_content(8196)))
    else :
        raw_results.update({site_name : {"req_number": 1, "response_time":[response.elapsed.total_seconds()], "throughput" : [sum(len(chunk) for chunk in response.iter_content(8196))]}})
        print(raw_results)

def calculate_results():
    for site, value in raw_results.items():
        #print(site, value)
        responce_time_avg = sum(value.get("response_time")) / len(value.get("response_time"))
        throughput_avg = sum(value.get("throughput")) / len(value.get("throughput"))

        print(f"AVG Response time of {site}: {responce_time_avg}")
        print(f"AVG Throughput of {site}: {throughput_avg}")

def get_url_sitename(url_address):
    return url_address.split(".")[1]

# number of works in the pool
n_workers = 10
# max number of queued tasks
n_queue = 10
# semaphore to limit the queue size to the pool
semaphore = Semaphore(n_queue)
# create the thread pool
with ThreadPoolExecutor(n_workers) as executor:
    # submit many tasks
    duration = 0
    duration_limit = 10
    start_time = time()
    stop_flag = True
    while stop_flag:
        futures = [submit_proxy(work, url_name, url_address) for url_name, url_address in input_urls.items()]
        if (time() - start_time) > 10:
             stop_flag = False


    # wait for all tasks to complete
    print('All tasks are submitted, waiting...')

print(raw_results)

calculate_results()
