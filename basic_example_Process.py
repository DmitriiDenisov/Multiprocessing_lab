from multiprocessing import Process, Queue, current_process
import random


# This example might be good for a run-and-done type of application

def rand_num(a: str):
    print('I got letter {}'.format(a))
    num = random.random()
    print(current_process().name)
    print(num)


if __name__ == "__main__":
    queue = Queue()
    list_processes = ['A', 'B', 'C', 'D', 'E']

    processes = [Process(target=rand_num, args=(letter,)) for letter in list_processes]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
