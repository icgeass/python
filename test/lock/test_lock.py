#! /usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Lock
import time
import threading

mutex = Lock()


def test_lock(tid):
    global mutex

    try:
        if mutex.acquire(False) is False:
            print 'acquire False' + tid
            return
        else:
            print 'acquire True' + tid
            time.sleep(1)
    except Exception as e:
        print 'ex' + tid
    finally:
        if mutex.locked():
            mutex.release()
            print 'release lock' + tid


if __name__ == '__main__':
    threading.Thread(target=test_lock, args=('1',)).start()
    threading.Thread(target=test_lock, args=('2',)).start()
    threading.Thread(target=test_lock, args=('3',)).start()
    print 'ok'
