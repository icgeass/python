#! /usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Condition
import threading

# https://www.anshu.com/p/5d257
# https://www.cnblogs.com/yoyoketang/p/8337118.html


'''
acquire([timeout])/release(): 调用关联的锁的相应方法。 
wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。
    使用前线程必须已获得锁定，否则将抛出异常。 
notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用
    acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会
    释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池
    尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

作者：StormZhu
链接：https://www.jianshu.com/p/5d2579938517
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''


class CountDownLatch:

    def __init__(self, count):
        self.count = count
        self.condition = Condition()

    def await(self):
        try:
            self.condition.acquire()  # 获得的是同一个共享锁
            while self.count > 0:
                print '----await: wait begin'
                self.condition.wait()  # 拿到锁也不要，还回去给其他线程，自己进入等待池等待通知
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
