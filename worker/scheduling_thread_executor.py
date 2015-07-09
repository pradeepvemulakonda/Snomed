from queue import Queue
import itertools
from worker.neo4j_scheduling_upload_worker import Neo4jSchedulingUploadWorker

__author__ = 'pradeepv'


class SchedulingThreadExecutor(object):
    def __init__(self, no_of_threads):
        self.no_of_threads = no_of_threads| 4
        print('Starting threads: ' + str(self.no_of_threads))

    def execute(self, item_generator, item_processor):
        # Create a queue to communicate with the worker threads
        try:
            queue = Queue()
            threads = []
            # Create 8 worker threads
            for x in range(self.no_of_threads):
                worker = Neo4jSchedulingUploadWorker(queue, item_processor)
                # Setting daemon to True will let the main thread exit even though the workers are blocking
                worker.daemon = True
                worker.start()
                threads.append(worker)
            # Put the tasks into the queue as a tuple
            previousId = None
            round_robin_thread_list = itertools.cycle(threads)
            currentThread = next(round_robin_thread_list)
            for item in item_generator.generate:
                if item['sourceId'] == previousId:
                    queue.put((item, currentThread.name))
                else:
                    currentThread = next(round_robin_thread_list)
                    queue.put((item, currentThread.name))

            # Causes the main thread to wait for the queue to finish processing all the tasks
            queue.join()

            # stop workers
            for i in range(self.no_of_threads):
                queue.put(None)
            for t in threads:
                t.join()
        finally:
            print('In the finally')
            item_generator.close()
            for i in range(self.no_of_threads):
                queue.put(None)
            for t in threads:
                t.join()

