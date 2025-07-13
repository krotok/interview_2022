import random
import time
import multiprocessing
from multiprocessing.queues import SimpleQueue
from multiprocessing import Queue

import requests

input_urls = {
    #"url1":"http://51.105.241.115/interview_app_1/",
    #"url2":"http://51.105.241.115/interview_app_2/",
    #"url3":"http://51.105.241.115/interview_app_1/sample?test=4000",
    #"url4":"http://51.105.241.115/interview_app_2/sample?test=4000",
    "url5":"http://www.facebook.com",
    "url6":"http://www.google.com",
    "url7":"http://www.walla.com"
}
conf = {}
conf['timeout_in_seconds'] = 5
conf['process_upper_bound_in_seconds'] = 8
conf['num_of_simultaneous_processes'] = 30

def send_get_request(url):
  response = requests.get(url)
  print(f"{url} get {response.status_code}")
  return requests.get(url)

def empty_the_queue(output_queue):
  while not output_queue.empty():
    #print('flushing message: {}'.format(output_queue.get()))
    current_request = output_queue.get()
    print(f"send: {current_request} request")
    send_get_request(current_request[1])
  print('done with flushings for this call')

def timeout_procs(procs, out_queue):
  '''
  No matter what, ALL the processes are:
  - either joined
  - or terminated and joined
  '''
  timeout_in_seconds = conf['timeout_in_seconds']
  start = time.time()
  while time.time() - start <= timeout_in_seconds:
    if any(p.is_alive() for p in procs):
      time.sleep(.1)  # Just to avoid hogging the CPU
      empty_the_queue(out_queue) # TODO attention here! maybe avoid this!!!
    else:
      # All the processes are done, break now.
      print('yuppie! all the processes finished on time! :)')
      for p in procs:
        print('stopping process {}'.format(p.name))
        p.join() # make sure things are stopped properly
        empty_the_queue(out_queue)
      break
  else:
    # We only enter this if we didn't 'break' above during the while loop!
    print("timed out, killing all processes")
    for p in procs:
      if not p.is_alive():
        print('this process is already finished: {}'.format(p.name))
      else:
        print('this process MUST be killed: {} (timeout of {} seconds has passed)'.format(p.name, timeout_in_seconds))
        p.terminate()
      print(' -> stopping (joining) process {}'.format(p.name))
      p.join()
      empty_the_queue(out_queue)

def put_to_queue(num, output_queue):
  print('started put_to_queue {}'.format(num))
  start_time = time.time()
  seconds_chunks_counter = 1
  while seconds_chunks_counter <= conf['process_upper_bound_in_seconds']:
    the_IO_intensive_task = random.random() # this could be a network call that hangs for too much time
    time.sleep(the_IO_intensive_task)
    #output_queue.put('put_to_queue {}: done with {} out of {}'.format(num, seconds_chunks_counter, conf['process_upper_bound_in_seconds']))

    output_queue.put(random.choice(list(input_urls.items())))
    seconds_chunks_counter += 1
  elapsed_time = time.time() - start_time
  print('finished put_to_queue {} after {} seconds'.format(num, elapsed_time))

def start_procs(num_procs, out_queue):
  procs = []
  for i in range(num_procs):
    proc_idx = i+1 # so e.g. for 10 processes: index is from 1 (included) to 11 (excluded i.e. 10 included)
    p = multiprocessing.Process(target=put_to_queue, args=(proc_idx,out_queue), name=('process_' + str(proc_idx)))
    procs.append(p)
    p.start()
    print('starting process {}'.format(p.name))
  return procs

def orchestrate_multi_processes():
  print('the current configuration is: {}'.format(conf))
  num_procs = conf['num_of_simultaneous_processes']
  output_q = Queue()
  procs = start_procs(num_procs, output_q)
  timeout_procs(procs, output_q)

if __name__ == "__main__":
  orchestrate_multi_processes()