from multiprocessing import Process, Queue, current_process
import numpy as np
import pandas as pd
import time


def return_np_array(a: int, b: int, queue):
    name = current_process().name
    print(name, 'Starting')
    time.sleep(3)
    queue.put(np.random.randint(low=a, high=b, size=5))  # we're putting return value into queue


def return_pd(a: int, b: int, queue):
    name = current_process().name
    print(name, 'Starting')
    time.sleep(4)
    queue.put(pd.DataFrame({'A': [1, 2, 3], 'B': [-1, 0.3, 3]}))


def return_string(a: int, b: int, queue):
    name = current_process().name
    print(name, 'Starting')
    time.sleep(4)
    queue.put('UID')


if __name__ == '__main__':
    queue = Queue()  # create a queue object

    service = Process(
        name='numpy',
        target=return_np_array,
        args=(11, 15, queue)
    )
    worker_1 = Process(
        name='pandas',
        target=return_pd,
        args=(0, 5, queue)
    )
    worker_2 = Process(  # default name
        target=return_string,
        args=(6, 11, queue)
    )

    processes = [worker_1, worker_2, service]
    for p in processes:
        p.start()
    # worker_1.start()
    # worker_2.start()
    # service.start()

    results_dict = {p.name: queue.get() for p in processes}  # Get results from Queue
    # results = [queue.get() for p in processes]  # Or we can get all values inside list

    # print(results)
    print(results_dict)
    types = [type(x) for x in results_dict.values()]  # Get types of all variables
    print(types)
