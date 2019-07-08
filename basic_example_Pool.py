from multiprocessing import Pool


# In the file basic_example_Process.py we looked at how we could spin up individual processes
# This might be good for a run-and-done type of application
# But when it comes to longer running applications, it is better to create a pool of longer running processes

def doubler(number):
    return number * 2


if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
