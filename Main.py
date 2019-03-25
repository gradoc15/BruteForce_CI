import  threading
import  queue

from PwdProducer import PwdProducer
from PwdConsumer import PwdConsumer

queue = queue.Queue(maxsize=100)
condition = threading.Condition()

producer = PwdProducer(queue,condition,4)

producer.start()
producer.join()

while(True):
    PwdConsumer(queue,condition).start()



