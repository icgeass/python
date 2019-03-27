#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
from os import path

import json


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


def test_json():
    obj = {"array": [1, 2, 3], "boolean": True, "color": "#82b92c", "null": None, "number": 123,
           "object": {"a": "b", "c": "d", "e": "f"}, "string": "Hello World"}
    with open(path.dirname(__file__) + '/test.json',
              'w') as json_file:
        json.dump(obj, json_file, cls=DecimalEncoder)
    json_str = json.dumps(obj)
    print('json.dumps: %s' % json_str)
    obj2 = json.loads(json_str)
    print('obj2: %s' % obj2)


if __name__ == '__main__':
    test_json()
