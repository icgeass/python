#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(logic, preset_value, collect_value):
    logic = logic.upper()
    compare_values = []
    if isinstance(collect_value, list) or isinstance(collect_value, tuple):
        compare_values.extend(collect_value)
    else:
        compare_values.append(collect_value)

    if logic == "GT":
        return do_check_int(any, lambda x, y: x > y, compare_values, preset_value)
    if logic == "GE":
        return do_check_int(any, lambda x, y: x >= y, compare_values, preset_value)
    if logic == "LT":
        return do_check_int(any, lambda x, y: x < y, compare_values, preset_value)
    if logic == "LE":
        return do_check_int(any, lambda x, y: x <= y, compare_values, preset_value)
    if logic == "EQ":
        return do_check_int(any, lambda x, y: x == y, compare_values, preset_value)
    if logic == "NE":
        return do_check_str(any, lambda x, y: x != y, compare_values, preset_value)
    if logic == "CONTAINS":
        return do_check_str(any, lambda x, y: y in x, compare_values, preset_value)
    if logic == "ANYSTARTWITH":
        return do_check_str(any, lambda x, y: x.startswith(y), compare_values, preset_value)
    if logic == "ALLSTARTWITH":
        return do_check_str(all, lambda x, y: x.startswith(y), compare_values, preset_value)

    return False


def do_check_int(checking, express, compare_values, preset_value):
    return do_check(checking, express, compare_values, preset_value, int)


def do_check_str(checking, express, compare_values, preset_value):
    return do_check(checking, express, compare_values, preset_value, str)


def do_check(checking, express, compare_values, preset_value, convert):
    return checking([express(convert(x), convert(preset_value)) for x in compare_values])


if __name__ == '__main__':
    print check('gt', 1, 2)
    print check('gt', 1, 0)
    print check('eq', 1, 0)
    print check('eq', 1, 1)
    print check('allstartwith', 1, (10, 2,))
    print check('anystartwith', 1, (10, 2,))