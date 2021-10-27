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
    pass  # 占坑，有时间补，教材P221


def gcd_iteration(a, b):
    """
    迭代法计算两个数的最大公约数: a = q * b + r

    :param a: int
    :param b: int
    :return: int
    """
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
    递归法计算两个数的最大公约数: a = q * b + r

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
    递归实现扩展欧几里得算法: ed = 1 (mod n)

    :param a: e(int)
    :param b: n(int)
    :return: gcd, x, y (x即是e^-1，也就是d)(int, int, int)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = InvMod(b, a % b)
        t = x
        x = y
        y = t - a // b * y
        return gcd, x, y


def ExpMod(a, b, n):
    """
    模指运算: a^b (mod n)

    :param a: int
    :param b: int
    :param n: int
    :return: int
    """
    b = bin(b)[2:]  # 获取二进制，去掉开头的'0b'
    # 快速平方乘算法得到列表
    L = [a]
    for i in range(len(b) - 1):
        a = a * a
        L.append(a)
    L.reverse()  # 列表反转，与二进制位对应
    # 对二进制值中为1的项相乘并模n
    res = 1
    for i in range(len(b)):
        if b[i] == '1':
            # 边乘边模
            res *= L[i]
            res %= n
    return res


def factor(num):
    """
    Calculates the lowest prime factor by default

    :param num: int
    :return: int
    """
    if num == 2 or num % 2 == 0:
        return 2
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):  # I could iterate over a list of primes
            if num % i == 0:  # But creating that list of primes turns out even more intensive task
                return i
        else:
            return num


def prime_check(num):
    """
    判断是否是素数，参考Python第三方库primePy

    :param num: int
    :return: bool: 是素数返回True，否则返回False
    """
    # from primePy import primes
    # primes.check()

    if factor(num) == num:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
