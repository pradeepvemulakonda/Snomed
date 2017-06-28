from queue import Queue
from threading import Thread
import time

__author__ = 'pradeepv'


class Neo4jSchedulingUploadWorker(Thread):
    num_worker_threads = 8
    value = 0

    def __init__(self, queue, item_processor):
        Thread.__init__(self)
        self.queue = queue
        self.tx = None
        self.idx = 0
        self.item_processor = item_processor
        self.daemon = True

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            item, name = self.queue.get()
            if(name != self.name):
                self.queue.put((item, name))
                continue
            time.sleep(0.2)
            if item is None:
                break
            if self.idx % 1000 == 0 and self.idx != 0:
                if self.tx is not None:
                    self.tx.commit()
                self.tx = self.item_processor.graph.begin()
                print('committed 1000 rows till row:' + str(self.idx))
            if self.idx == 0:
                self.tx = self.item_processor.graph.begin()
            self.idx += 1
            self.item_processor.process(item, self.tx)
            self.queue.task_done()
