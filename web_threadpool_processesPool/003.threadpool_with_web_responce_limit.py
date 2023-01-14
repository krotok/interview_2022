#This code block is nearly identical to the one we used in Step 2, but it has two key differences:
#We now pass timeout=0.00001 to get_wiki_page_existence. Since the requests package won’t be able to complete its web request to Wikipedia in 0.00001 seconds, it will raise a ConnectTimeout exception.
#We catch ConnectTimeout exceptions raised by future.result() and print out a string each time we do so.

import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status

wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(
            executor.submit(
                get_wiki_page_existence, wiki_page_url=url, timeout=0.00001
            )
        )
    for future in concurrent.futures.as_completed(futures):
        try:
            print(future.result())
        except requests.ConnectTimeout:
            print("ConnectTimeout.")