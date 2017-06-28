from queue import Queue
from worker.neo4j_upload_worker import Neo4jUploadWorker

__author__ = 'pradeepv'


class ThreadExecutor(object):
    def __init__(self, no_of_threads=4):
        self.no_of_threads = no_of_threads
        print('Starting threads: ' + str(self.no_of_threads))

    def execute(self, item_generator, item_processor):
        # Create a queue to communicate with the worker threads
        try:
            queue = Queue()
            threads = []
            # Create 8 worker threads
            for x in range(self.no_of_threads):
                worker = Neo4jUploadWorker(queue, item_processor)
                # Setting daemon to True will let the main thread exit even though the workers are blocking
                worker.daemon = True
                worker.start()
                threads.append(worker)
            # Put the tasks into the queue as a tuple
            for item in item_generator.generate:
                queue.put(item)
            # Causes the main thread to wait for the queue to finish processing all the tasks
            queue.join()

            # stop workers
            for i in range(self.no_of_threads):
                queue.put(None)
            for t in threads:
                t.join()
        except:
            try:
                print('In the exception claue')
                item_generator.close()
                for i in range(self.no_of_threads):
                    queue.put(None)
                for t in threads:
                    t.join()
            except:
                print("ignore exception in catch")
        finally:
            print('In the finally')
            item_generator.close()