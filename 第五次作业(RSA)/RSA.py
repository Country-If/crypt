#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import math


def is_prime(n):
    """
    试除法判断整数n是否是素数

    :param n: int
    :return: bool：是素数返回True，否则返回False
    """
    i = 2  # 从2开始穷举
    while i <= math.sqrt(n):  # 穷举到sqrt(n)
        if n % i == 0:  # 是素数
            return False
        i += 1
    return True


def gcd_iteration(a, b):
    """
    迭代法计算两个数的最大公约数

    :param a: int
    :param b: int
    :return: int
    """
    # a = q * b + r
    while True:
        r = a % b  # Calculate the remainder
        if r == 0:
            break
        # Change the value of a and b
        a = b
        b = r
    return b


def gcd_recursion(a, b):
    """
    递归法计算两个数的最大公约数

    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)


if __name__ == '__main__':
    import random

    for i in range(10):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print(a)
        print(b)
        print(gcd_recursion(a, b))
        print()
