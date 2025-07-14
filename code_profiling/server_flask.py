from flask import Flask
import threading
import time
import math
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=2)

def cpu_bound_task():
    print("[CPU Thread] Starting heavy computation")
    while True :
        result = 0
        for i in range(10**7):
            result += math.sqrt(i)
        print("[CPU Thread] Finished computation")

def start_cpu_thread():
    executor.submit(cpu_bound_task)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/start-task')
def start_task():
    thread = threading.Thread(target=start_cpu_thread)
    thread.start()
    return "Started CPU-bound task in background thread."

if __name__ == '__main__':
    app.run(port=5000)
