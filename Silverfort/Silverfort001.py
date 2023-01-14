from multiprocessing import Semaphore

import requests
import concurrent.futures

input_urls = {
    #"url1":"http://51.105.241.115/interview_app_1/",
    #"url2":"http://51.105.241.115/interview_app_2/",
    #"url3":"http://51.105.241.115/interview_app_1/sample?test=4000",
    #"url4":"http://51.105.241.115/interview_app_2/sample?test=4000",
    "url5":"http://www.facebook.com"
}

semaphore = Semaphore(10)

# callback for completed tasks
def task_complete_callback(future):
    global semaphore
    # release the semaphore
    semaphore.release()

def submit_proxy(function, *args, **kwargs):
    global semaphore, executor
    # acquire the semaphore, blocks if occupied
    semaphore.acquire()
    # submit the task normally
    future = executor.submit(function, *args, **kwargs)
    # add the custom done callback
    future.add_done_callback(task_complete_callback)
    return future

def send_request(page_url, timeout=100):
    response = requests.get(url=page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return page_url + " - " + page_status + " " + str(response.elapsed.total_seconds()) + " " + str(sum(len(chunk) for chunk in response.iter_content(8196)))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = []

    for url in input_urls.values():
        #print(index,url)
        futures.append(
            executor.submit(
                send_request, page_url=url, timeout=100
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except requests.ConnectTimeout:
            print("ConnectTimeout.")

