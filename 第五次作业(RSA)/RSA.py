#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


import math


def is_prime(n):
    """
    穷举法判断整数n是否是素数

    :param n: 整数n
    :return: 是素数返回True，否则返回False
    """
    i = 2   # 从2开始穷举
    while i <= math.sqrt(n):    # 穷举到sqrt(n)
        if n % i == 0:  # 是素数
            return False
        i += 1
    return True


if __name__ == '__main__':
    for i in range(100):
        if is_prime(i):
            print(i)
