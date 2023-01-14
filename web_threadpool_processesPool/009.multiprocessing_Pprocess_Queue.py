import multiprocessing


def hold(url):
    ...
    return soup

def queue(url):
    ...
    return bool(li)

def update(url):
    with multiprocessing.Pool(2) as pool:
        hold_job = pool.apply_async(hold, args=[url])
        queue_job = pool.apply_async(queue, args=[url])

        # block until hold_job is done
        soup = hold_job.get()
        # block until queue_job is done
        li = queue_job.get()