from queue import Queue
from threading import Thread
import time

__author__ = 'pradeepv'


class Neo4jUploadWorker(Thread):
    num_worker_threads = 8
    value = 0

    def __init__(self, queue, item_processor):
        Thread.__init__(self)
        self.queue = queue
        self.tx = None
        self.idx = 0
        self.item_processor = item_processor

    def run(self):
        try:
            while True:
                # Get the work from the queue and expand the tuple
                item = self.queue.get()
                if item is None:
                    break
                if self.idx % 1000 == 0 and self.idx != 0:
                    if self.tx is not None:
                        time.sleep(0.2)
                        self.tx.commit()
                    self.tx = self.item_processor.graph.begin()
                    print('committed 1000 rows till row:' + str(self.idx))
                if self.idx == 0:
                    self.tx = self.item_processor.graph.begin()
                self.idx += 1
                self.item_processor.process(item, self.tx)
                self.queue.task_done()
        finally:
            print('in the worker finally')
            if self.tx is not None and not self.tx.finished:
                self.tx.commit()
