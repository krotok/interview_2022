from multiprocessing import Process,Pool
import time

import requests

raw_results = dict()
results = dict()

input_urls = {
    "url1":"http://51.105.241.115/interview_app_1/",
    "url2":"http://51.105.241.115/interview_app_2/",
    "url3":"http://51.105.241.115/interview_app_1/sample?test=4000",
    "url4":"http://51.105.241.115/interview_app_2/sample?test=4000",
    # "url5":"http://www.facebook.com",
    # "url6":"http://www.google.com",
    # "url7":"http://www.walla.com"
}

def get_url_sitename(url_address):
    return url_address.split(".")[1]

def send_request(page_url, timeout=10):
    response = requests.get(url=page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    #print(page_url + " - " + page_status + " " + str(response.elapsed.total_seconds()) + " " + str(sum(len(chunk) for chunk in response.iter_content(8196))))
    # site_name = get_url_sitename(page_url)
    # if site_name in raw_results:
    #     raw_results[site_name]["req_number"] = raw_results.get(site_name).get("req_number") + 1
    #     raw_results.get(site_name).get("response_time").append(response.elapsed.total_seconds())
    #     raw_results.get(site_name).get("throughput").append(sum(len(chunk) for chunk in response.iter_content(8196)))
    # else :
    #     raw_results.update({site_name : {"req_number": 1, "response_time":[response.elapsed.total_seconds()], "throughput" : [sum(len(chunk) for chunk in response.iter_content(8196))]}})
    #     print(raw_results)



if __name__ == '__main__':
    pool = Pool(processes=12)
    for url_name, url_address in input_urls.items():
        result = pool.apply_async(send_request, (url_address,))
        #print(result.get(timeout=1))


# issue tasks to the process pool asynchronously
result = map_async(task, items)