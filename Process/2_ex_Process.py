from multiprocessing import Process, current_process
import random


def rand_num(a: str):
    print('I got letter {}'.format(a))
    num = random.random()
    print(current_process().name)
    print(num)


if __name__ == "__main__":
    list_processes = ['A', 'B', 'C', 'D', 'E']

    # Just another method how to run processes via list comprehension
    processes = [Process(target=rand_num, args=(letter,)) for letter in list_processes]

    for p in processes:
        p.start()
