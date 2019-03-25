import threading
import queue
import itertools
import string

from Password import Password

class PwdConsumer(threading.Thread):
    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while(True):
            password = None
            self.condition.acquire()
            try:
                pw = self.queue.get(block=False)
                password = Password(pw)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
                print("no pwd")

                self.condition.release()

            #todo brute force algurithm implementation
            if not password is None:
                myLetters = string.ascii_letters + string.digits + string.punctuation
                for i in range(3, 5):
                    for j in map(''.join, itertools.product(myLetters, repeat=i)):
                        if password.check(test=str(j)):
                            print("password found: "+j)

