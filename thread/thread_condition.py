#! /usr/bin/env python
from threading import Condition
import threading

class CountDownLatch:

    def __init__(self, count):
        self.count = count
        self.condition = Condition()

    def await(self):
        try:
            self.condition.acquire()
            while self.count > 0:
                print '----await: wait begin'
                self.condition.wait()
                print '----await: wait end'
        finally:
            self.condition.release()

    def countDown(self, wait=False):
        try:
            self.condition.acquire()
            if wait:
                import time
                time.sleep(5)
            self.count -= 1
            self.condition.notifyAll()
        finally:
            self.condition.release()

    def getCount(self):
        return self.count


def test(id, countDown):
    print 'test begin: ' + str(id)
    wait = False
    if id == 1:
        wait = True
    countDown.countDown(wait)
    print 'test end: ' + str(id)


def test_await(id, countDown):
    print 'test_await begin: ' + str(id)
    countDown.await()
    print 'test_await end: ' + str(id)


if __name__ == '__main__':
    countDown = CountDownLatch(5)
    threading.Thread(target=test, args=(1, countDown,)).start()
    threading.Thread(target=test, args=(2, countDown,)).start()
    threading.Thread(target=test, args=(3, countDown,)).start()
    threading.Thread(target=test_await, args=(100, countDown,)).start()
    threading.Thread(target=test, args=(4, countDown,)).start()
    threading.Thread(target=test, args=(5, countDown,)).start()


    import time
    time.sleep(10)




