from datetime import datetime
import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from multiprocessing import Process, Pool, current_process
from time import time, sleep
from multiprocessing import set_start_method
from typing import List

import requests

logging.basicConfig(filename='log_file_name.log',format="%(module)s : %(funcName)s : (Process Details : (%(process)d, %(processName)s)\nLog Message : %(message)s\n",
                    datefmt="%d-%B,%Y %I:%M:%S %p",
                    level=logging.DEBUG)

raw_results = dict()
results = dict()
start_time = time()
run_flag = True

input_urls = {
    "url1":"http://51.105.241.115/interview_app_1/",
    "url2":"http://51.105.241.115/interview_app_2/",
    "url3_2":"http://51.105.241.115/interview_app_1/sample?test=2",
    "url3_500":"http://51.105.241.115/interview_app_1/sample?test=500",
    "url3_400":"http://51.105.241.115/interview_app_1/sample?test=4000",
    "url4_2":"http://51.105.241.115/interview_app_2/sample?test=2",
    "url4_500":"http://51.105.241.115/interview_app_2/sample?test=500",
    "url4_4000":"http://51.105.241.115/interview_app_2/sample?test=4000"
}

def get_url_sitename(url_address):
    return url_address.split(".")[1]

def send_requests(url_addresses: List = [], timeout=10):
    sleep(3)
    logging.info(f"FROM SEND_REQUESTS:{url_addresses}")
    worker_id = current_process().pid
    logging.info(f"Worker {worker_id} received id: {url_addresses}")
    for url_address in url_addresses:
        response = requests.get(url=url_address, timeout=timeout)
    logging.info(f"MAP {response.text}")
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
        return(response)
    elif response.status_code == 404:
        page_status = "does not exist"

    # print(page_url + " - " + page_status + " " + str(response.elapsed.total_seconds()) + " " + str(sum(len(chunk) for chunk in response.iter_content(8196))))

def timer(max_duration = 30):
    global run_flag
    if (time() - start_time) > max_duration:
        logging.info(f"Time: {time() - start_time}")
        run_flag = False
    sleep(1)

def add_results(result):

    site_name = result[0] #get_url_sitename(page_url)
    response = result[1]
    if site_name in raw_results:
        raw_results[site_name]["req_number"] = raw_results.get(site_name).get("req_number") + 1
        raw_results.get(site_name).get("response_time").append(response.elapsed.total_seconds())
        raw_results.get(site_name).get("throughput").append(sum(len(chunk) for chunk in response.iter_content(8196)))
        logging.info(raw_results)
    else:
        raw_results.update({site_name: {"req_number": 1, "response_time": [response.elapsed.total_seconds()],
                                        "throughput": [sum(len(chunk) for chunk in response.iter_content(8196))]}})
        logging.info(raw_results)

def worker(pool,input_urls):
    url_names = []
    url_addresses = []
    logging.info(f"WORKER input_urls:{input_urls}")
    for url_name, url_address in input_urls.items():
        url_names.append(str(url_name))
        url_addresses.append(str(url_address))
    print(f"URL_ADDRESSES:{url_addresses}")
    #url_addresses = ["http://51.105.241.115/interview_app_1/"]
    map_result = pool.apply_async(send_requests, [url_addresses],)
    logging.info(f"MAP {map_result}")
    map_result.wait()
    results = map_result.get()
    for result in results:
        print(f"Results: {result}")

if __name__ == "__main__":
    logging.info("Start Time : {}".format(datetime.now()))
    set_start_method('spawn')
    timer_process = Process(target=timer)
    timer_process.start()

    # Why only 2 processes in the pool?:
    pool = Pool(processes=12)

    while run_flag:

        worker(pool, input_urls)




        # pool.apply_async(do_something, args=('a',))
        # pool.apply_async(do_something, args=('b',))
        # pool.apply_async(do_something, args=('c',))
        # server_address = ("", 8000)
        # httpd = ThreadingHTTPServer(server_address, BaseHTTPRequestHandler)
        #     try:
        #         # httpd.serve_forever()
        #         print(result)
        #     except (KeyboardInterrupt, SystemExit):
        #         pass

        # Wait for submitted tasks to complete:
        pool.close()
        pool.join()
    timer_process.join()