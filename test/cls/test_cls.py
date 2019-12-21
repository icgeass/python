#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json


class TestClass(object):

    def __init__(self, a, b, c=None, *args, **kwargs):
        self.a = a
        self.b = b
        self.c = c
        self.args = args
        self.kwargs = kwargs


if __name__ == '__main__':
    json_str = '{"a": "a", "b": 2, "no": "test"}'
    t = TestClass(**json.loads(json_str))
    print t.__dict__
