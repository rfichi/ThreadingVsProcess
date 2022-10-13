from threading import Lock


class Counter:
    counter = 0

    def __init__(self):
        self.lock = Lock()

    def increase(self, by):

        self.lock.acquire()

        local_counter = self.counter
        local_counter += by

        self.counter = local_counter

        self.lock.release()


