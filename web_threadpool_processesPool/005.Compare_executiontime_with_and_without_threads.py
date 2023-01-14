import time
import requests
import concurrent.futures


def get_wiki_page_existence_nothreads(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

def get_wiki_page_existence_with_threads(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

###########MAIN##############
wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

print("Running without threads:")
without_threads_start = time.time()
for url in wiki_page_urls:
    print(get_wiki_page_existence_nothreads(wiki_page_url=url))
print("Without threads time:", time.time() - without_threads_start)

print("Running threaded:")
threaded_start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(get_wiki_page_existence_with_threads, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
print("Threaded time:", time.time() - threaded_start)