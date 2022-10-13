import concurrent.futures
import time
from multiprocessing import freeze_support
from threading import Thread, Lock
from time import sleep

from classes import Counter

counter = 0


def increase(by, lock):
    global counter

    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}\n')

    lock.release()


if __name__ == "__main__":
    # freeze_support()
    counter = Counter()

    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(counter.increase, range(5))

    end = time.perf_counter()
    print(f"The final counter is {counter.counter}, execution time was {round((end - start), 2)}")
