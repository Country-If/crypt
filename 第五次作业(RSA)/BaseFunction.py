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


def is_prime_probability_test(n):
    """素数的概率性检验算法"""
    pass    # 占坑，有时间补，教材P221


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


def InvMod(a, b):
    """
    递归实现扩展欧几里得算法 ed = 1 (mod n)

    :param a: e
    :param b: n
    :return: gcd, x, y (x即是e^-1，也就是d)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = InvMod(b, a % b)
        t = x
        x = y
        y = t - a // b * y
        return gcd, x, y


if __name__ == '__main__':
    import random

    for i in range(10):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        print(a)
        print(b)
        print(InvMod(a, b))
        print()
