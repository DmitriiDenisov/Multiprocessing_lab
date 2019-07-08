from multiprocessing import Pool
from multiprocessing import current_process
from time import sleep


# In the file 2_ex_Process.py we looked at how we could spin up individual processes
# This might be good for a run-and-done type of application
# But when it comes to longer running applications, it is better to create a pool of longer running processes

def doubler(number):
    print(current_process().name)
    sleep(1)  # imitating working of process
    return number * 2


if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    list_ans = pool.map(doubler, numbers)
    print(list_ans)
