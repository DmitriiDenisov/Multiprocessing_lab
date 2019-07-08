from multiprocessing import Process, Queue, current_process
from random import random, randint
# import multiprocessing
import time


def worker(a: int, b: int, queue):
    name = current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')
    random_n = randint(a, b)
    queue.put(random_n)  # we're putting return value into queue


def my_service(a: int, b: int, queue):
    name = current_process().name
    print(name, 'Starting')
    time.sleep(4)
    print(name, 'Exiting')
    random_n = random()
    queue.put(random_n)  # we're putting return value into queue


if __name__ == '__main__':
    queue = Queue()  # create a queue object

    service = Process(
        name='my_service',
        target=my_service,
        args=(-1, -1, queue)
    )
    worker_1 = Process(
        name='worker 1',
        target=worker,
        args=(0, 5, queue)
    )
    worker_2 = Process(  # default name
        target=worker,
        args=(6, 11, queue)
    )

    processes = [worker_1, worker_2, service]
    for p in processes:
        p.start()
    # worker_1.start()
    # worker_2.start()
    # service.start()

    results = [queue.get() for p in processes]
    print(results)
