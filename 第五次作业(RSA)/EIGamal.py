#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *
import random


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


class EIGamal:
    def __init__(self, n_digit):
        self.p, self.g = generate_p_g(n_digit)

    def generate_key(self):
        """
        生成双方的公钥和私钥

        :return: (A_private, A_public, B_private, B_public)
        """
        A_private = random.randint(2, self.p - 2)  # 随机选择私钥
        B_private = random.randint(2, self.p - 2)
        A_public = ExpMod(self.g, A_private, self.p)  # 计算公钥
        # A_public = pow(self.g, A_private, self.p)
        B_public = ExpMod(self.g, B_private, self.p)
        # B_public = pow(self.g, B_private, self.p)
        return A_private, A_public, B_private, B_public

    def encrypt(self, private_key, public_key, M):
        """
        加密算法

        :param private_key: int，自己的私钥
        :param public_key: int，对方的公钥
        :param M: int，原始数据
        :return: (int, int)，密文(C1, C2)
        """
        U = ExpMod(public_key, private_key, self.p)  # 由对方的公钥生成
        C1 = ExpMod(self.g, private_key, self.p)  # 由自己的私钥生成公钥
        C2 = (U * M) % self.p  # 加密后的内容
        return C1, C2  # 发送的密文

    def decrypt(self, private_key, public_key, C):
        pass


if __name__ == '__main__':
    n = int(input("input n: "))
    # print(generate_p_g(n))
    eigamal = EIGamal(n)
    a_private, a_public, b_private, b_public = eigamal.generate_key()
    m = int(input("input data: "))
    print(eigamal.encrypt(a_private, b_public, m))
