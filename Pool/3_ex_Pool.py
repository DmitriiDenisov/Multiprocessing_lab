import multiprocessing as mp
from time import sleep


def my_func(x):
    print(mp.current_process().name)
    sleep(0.5)
    return x ** x


def main():
    pool = mp.Pool(mp.cpu_count())
    # Now we will get results from our processes
    result = pool.map(my_func, [4, 2, 3, 5, 3, 2, 1, 2])
    print(result)
    result_set_2 = pool.map(my_func, [4, 6, 5, 4, 6, 3, 23, 4, 6])

    print(result_set_2)


if __name__ == "__main__":
    main()
