from datetime import datetime
from multiprocessing import set_start_method, Process
from multiprocessing import Process, Event
import Timer
import logging
from time import sleep

logging.basicConfig(filename='log_file_name.log',format="%(module)s : %(funcName)s : (Process Details : (%(process)d, %(processName)s)\nLog Message : %(message)s\n",
                    datefmt="%d-%B,%Y %I:%M:%S %p",
                    level=logging.DEBUG)


class TimerProcess(Process):
    def __init__(self, interval, function, args=[], kwargs={}):
        super(TimerProcess, self).__init__()
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet"""
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()

def print_time(self,param):
    sleep(10)
    logging.info("Current Time : {}".format(datetime.now()))


if __name__ == "__main__":
    logging.info("Start Time : {}".format(datetime.now()))
    duration = TimerProcess(10, print_time, ["123"])
    duration.run()
    logging.info("Finished Time : {}".format(datetime.now()))