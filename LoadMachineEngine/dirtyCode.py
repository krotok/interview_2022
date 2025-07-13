import multiprocessing
import random
import time

def writer(test_duration, input_urls):
    test_running_flag = True
    start_time = time.time()
    while test_running_flag:
        print(f"process {multiprocessing.current_process.__name__} url {random.choice(input_urls)} duration {time.time() - start_time}")
        if time.time() - start_time < test_duration:
            test_running_flag = False
        time.sleep(1)

def start_writer_process(test_duration,input_urls):
    processes = []
    #for i in range(0, 10):
    p = multiprocessing.Process(target=writer, args=(test_duration,input_urls,))
    #    processes.append(p)
    p.start()

    time.sleep(1)
    #for process in processes:
    p.join()

if __name__ == "__main__":
    input_urls = {
        # "url1":"http://51.105.241.115/interview_app_1/",
        # "url2":"http://51.105.241.115/interview_app_2/",
        # "url3":"http://51.105.241.115/interview_app_1/sample?test=4000",
        # "url4":"http://51.105.241.115/interview_app_2/sample?test=4000",
        "url5": "http://www.facebook.com",
        "url6": "http://www.google.com",
        "url7": "http://www.walla.com"
    }

    test_duration = 10
    start_writer_process(test_duration, input_urls)