#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import math
import random

min_size = 5  # 二进制位数最小值


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
    """
    素数的概率性检验算法

    :param n: int
    :return: bool：是素数返回True，否则返回False
    """
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
        raise ValueError("n太小了，n必须大于" + str(min_size) + "，n值建议小于50")
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


def generate_prime(n_digit):
    """
    随机生成n位的素数

    :param n_digit: int，素数位数
    :return: int，n位素数
    """
    if n_digit < 1:
        raise ValueError("素数位数不能小于1")
    rand_list = random.sample([str(i) for i in range(1, 10)], 9)  # 初始化1-9的不重复列表，防止生成类似999的整数，影响后续操作
    randint_list = rand_list[: n_digit]
    if n_digit > 9:  # 超过位数则补齐
        while len(randint_list) < n_digit:
            randint_list.append(str(random.randint(0, 9)))
    randint = int("".join(randint_list))  # 转为整数
    while not prime_check(randint):  # 得到素数
        randint += 1
    return randint


def generate_p_g(n_digit):
    """
    生成大素数p及其本原元g

    :param n_digit: int，素数位数
    :return: (p, q), (int, int)
    """
    while True:
        q = generate_prime(n_digit)  # 随机生成一个n位的素数q
        if prime_check(2 * q + 1):  # 判断 2*q+1 是否为素数
            p = 2 * q + 1
            break
    while True:
        g = random.randint(2, p - 2)  # 随机选取整数g，g范围：(1, p - 1)
        if ExpMod(g, 2, p) != 1 and pow(g, q, p) != 1:  # 左边用了自己写的模指运算函数，右边用Python自带函数速度快一点
            break
    return p, g


if __name__ == '__main__':
    pass
