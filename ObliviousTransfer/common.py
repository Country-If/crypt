#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import math
import random

min_size = 7


def ExGcd(e, n):
    """
    递归实现扩展欧几里得算法: ed ≡ 1 (mod n) <=> ed + ny = 1

    :param e: int
    :param n: int
    :return: gcd, d, y (int, int, int)
    """
    if n == 0:
        return e, 1, 0
    else:
        gcd, d, y = ExGcd(n, e % n)
        t = d
        d = y
        y = t - e // n * y
        return gcd, d, y


def ExpMod(a, b, n, debug=False, debug_all=False):
    """
    模指运算(快速平方乘算法): a^b (mod n)

    :param a: int
    :param b: int
    :param n: int
    :param debug: bool (default False)
    :param debug_all: bool (default False)
    :return: int
    """
    a_ = a
    b_bin = bin(b)[2:]  # 获取二进制，去掉开头的'0b'
    # 平方乘后的存放列表
    L = [a_]
    for i in range(len(b_bin) - 1):
        a_ = a_ * a_ % n  # 边乘边模
        L.append(a_)
    L.reverse()  # 列表反转，与二进制位对应
    # 对二进制值中为1的项相乘并模n
    res = 1
    for i in range(len(b_bin)):
        if b_bin[i] == '1':
            # 边乘边模
            res *= L[i]
            res %= n
    if debug:
        print("Calculate: " + str(a) + "^" + str(b) + " mod " + str(n) + " = " + str(res))
    if debug_all:
        print("\n*********Debug mode***************")
        print("Calculate: " + str(a) + "^" + str(b) + " mod " + str(n))
        weight_list_calc = [2 ** i if b_bin[::-1][i] == '1' else 0 for i in range(len(b_bin) - 1, -1, -1)]
        weight_list_show = [2 ** i for i in range(len(b_bin) - 1, -1, -1)]
        print("b: " + str(b) + "(10) = " + b_bin + "(2) = " + "+".join([str(i) for i in weight_list_calc]))
        for i in range(len(L) - 1, -1, -1):
            if i == len(L) - 1:
                print(str(a) + "^" + str(weight_list_show[i]) + " mod " + str(n) + " = " + str(L[i]))
            else:
                print(str(a) + "^" + str(weight_list_show[i]) + " mod " + str(n) + " = " +
                      str(L[i + 1]) + "^2 mod " + str(n) + " = " + str(L[i]))
        print(str(a) + "^" + str(b) + " mod " + str(n) + " = ", end="")
        for i in range(len(L) - 1, -1, -1):
            if weight_list_calc[i] != 0 and i != 0:
                print(str(a) + "^" + str(weight_list_calc[i]), end=" x ")
            if weight_list_calc[i] != 0 and i == 0:
                print(str(a) + "^" + str(weight_list_calc[i]), end=" mod " + str(n) + " = ")
        for i in range(len(L) - 1, -1, -1):
            if weight_list_calc[i] != 0 and i != 0:
                print(str(L[i]), end=" x ")
            if weight_list_calc[i] != 0 and i == 0:
                print(str(L[i]), end=" mod " + str(n) + " = ")
        print(str(res))
        print("**********************************\n")
    return res


def _factor(num):
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

    return _factor(num) == num


def generate_p_q(n_bit):
    """
    随机生成二进制位数为n的大素数p、q

    :param n_bit: int，整数对应的二进制位数
    :return: (p, q)
    """
    # 随机生成n位二进制所对应的十进制整数
    if n_bit <= min_size:
        raise ValueError("n太小了，n必须大于%d，n值建议小于50" % min_size)
    randint_list = ['1'] * n_bit  # 初始化长度为n的列表
    # 随机更改数据的位置
    pos_list = random.sample(range(1, n_bit), random.randint(min_size, n_bit) - 1)
    for pos in pos_list:
        randint_list[pos] = '0'
    randint_str = ''.join(randint_list)  # 列表转字符串
    randint = int(randint_str, 2)  # 十进制值
    # 获取p, q
    while not prime_check(randint):
        randint += 1
    p = randint
    randint += random.randint(min_size, n_bit)  # 加上随机数得到新的随机整数
    while not prime_check(randint):
        randint += 1
    q = randint
    return p, q


def get_prime(n):
    """
    给定整数n，获取大于等于n的素数

    :param n: int
    :return: int
    """
    while not prime_check(n):
        n += 1
    return n


def generate_RSA_key(n_bit):
    p, q = generate_p_q(n_bit)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    # 随机选取e，满足1<e<phi_n，且(e, phi_n)=1
    e = get_prime(random.randint(2, int(str(phi_n)[: len(str(phi_n)) // 2])))
    d = ExGcd(e, phi_n)[1] % phi_n
    return n, e, d
