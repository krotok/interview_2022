from multiprocessing.dummy import Pool

import requests

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
    response = requests.get(url)
    return url, response.status_code

pool = Pool(10) # Creates a pool with ten threads; more threads = more concurrency.
                # "pool" is a module attribute; you can be sure there will only
                # be one of them in your application
                # as modules are cached after initialization.

if __name__ == '__main__':
    futures = []
    for x in range(100):
        futures.append(pool.apply_async(fetch, ['http://www.google.com']))
    # futures is now a list of 10 futures.
    for future in futures:
        print(future.get()) # For each future, wait until the request is
                            # finished and then print the response object.