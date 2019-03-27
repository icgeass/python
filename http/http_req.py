#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


def post(url=None, param_dict={}, timeout=3, json_type=False):
    if json_type:
        req = urllib2.Request(url=url, data=json.dumps(param_dict, cls=DecimalEncoder))
        req.add_header('Content-Type', 'application/json')
    else:
        req = urllib2.Request(url=url, data=urllib.urlencode(param_dict))
    res_data = urllib2.urlopen(req, timeout=timeout)
    result = res_data.read()
    return result


if __name__ == '__main__':
    print post('https://www.baidu.com')
