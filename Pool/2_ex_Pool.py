import multiprocessing as mp
from multiprocessing import current_process
from time import sleep


def my_func(x):
    print(current_process().name)
    sleep(1)
    print(x ** x)
    return x ** x


def main():
    n = mp.cpu_count()  # returns number of cores
    print(n)
    pool = mp.Pool(n)
    result = pool.map(my_func, [4, 2, 3, 5, 3, 0, -1])
    print(result)


if __name__ == "__main__":
    main()
