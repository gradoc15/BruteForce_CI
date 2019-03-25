import threading
import sys
from Password import Password
import queue
import random
import string

class PwdProducer(threading.Thread):
    def __init__(self, queue, condition, range):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition
        self.range = range

    def run(self):
        while(True):

            password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.range))
            self.condition.acquire()

            try:
                self.queue.put(password, block=False)
                self.condition.notify()
            except queue.Full:
                self.condition.wait()

            self.condition.release()