import time

class Timer:
    """
        Timer class
    """

    def __init__(self):
        self.start = time.time()

    '''
    Restarts the timer.
    '''

    def restart(self):
        self.start = time.time()

    '''
    Returns the time elapsed and resets the counter.
    '''

    def get_new_time(self):
        value = time.time() - self.start
        self.restart()
        return value

    '''
    Prints the time elapsed and resets the counter.
    '''

    def print_new_time(self):
        print(self.get_new_time())

    '''
    Returns the time elapsed (Does not reset the counter).
    '''

    def get_time(self):
        return time.time() - self.start
        self.restart()

    '''
    Prints the time elapsed (Does not reset the counter).
    '''

    def print_time(self):
        print(self.get_time())

    '''
    Returns the time elapsed in HH:mm:ss (Does not reset the counter).
    '''

    def get_time_hhmmss(self):
        end = time.time()
        m, s = divmod(end - self.start, 60)
        h, m = divmod(m, 60)
        time_str = "%02d:%02d:%02d" % (h, m, s)
        return time_str


timer = Timer()  # Initialize the timer
# wash clothes for 5 seconds
timer.print_time()  # Print the time elapsed since Initialization (in seconds)
# dry clothes for 3 seconds
timer.print_new_time()  # Print the time elapsed since Initialization and reset the timer
# burn clothes for 10 seconds
print(str('Task done for ' + str(timer.get_time()) + ' seconds.'))