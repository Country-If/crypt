#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *
import random

min_size = 10


def generate_p_q(n):
    """
    随机生成二进制位数为n的大素数p、q

    :param n: int，整数对应的二进制位数
    :return: (p, q)
    """
    # 随机生成n位二进制所对应的十进制整数
    if n <= min_size:
        raise ValueError("n太小了，n必须大于" + str(min_size) + "，n值建议小于50")
    randint_list = ['1'] * n  # 初始化长度为n的列表
    # 随机更改数据的位置
    pos_list = random.sample(range(1, n), random.randint(min_size, n) - 1)
    for pos in pos_list:
        randint_list[pos] = '0'
    randint_str = ''.join(randint_list)  # 列表转字符串
    randint = int(randint_str, 2)  # 十进制值
    print(randint)
    # 获取p, q
    while not prime_check(randint):
        randint += 1
    p = randint
    randint += random.randint(min_size, n)  # 加上随机数得到新的随机整数
    while not prime_check(randint):
        randint += 1
    q = randint
    return p, q


class RSA_Key:
    def __init__(self):
        pass


if __name__ == '__main__':
    print(generate_p_q(int(input("input bit num: "))))
