#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback


def err():
    try:
        1 / 0
    except Exception as e:
        print(traceback.format_exc(e))


if __name__ == '__main__':
    err()
