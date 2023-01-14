from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from multiprocessing import Pool, current_process


def do_something(item_id):
    worker_id = current_process().pid
    print(f"Worker {worker_id} received id: {item_id}")
    # long_term_operation_that_leaks_memory(item_id)
    # print(f"Worker {worker_id} completed id: {item_id}")

def main():
    # Why only 2 processes in the pool?:
    pool = Pool(processes=2)
    pool.apply_async(do_something, args=('a',))
    pool.apply_async(do_something, args=('b',))
    pool.apply_async(do_something, args=('c',))
    server_address = ("", 8000)
    httpd = ThreadingHTTPServer(server_address, BaseHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    # Wait for submitted tasks to complete:
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()