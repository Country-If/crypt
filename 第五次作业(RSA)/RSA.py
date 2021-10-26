#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *
import random

min_size = 10


def _generate_p_q(n_bit):
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


def get_prime(n):
    while not prime_check(n):
        n += 1
    return n


class RSA_Key:

    def __init__(self, n_bit):
        self.n_bit = n_bit
        self.__p, self.__q = _generate_p_q(self.n_bit)
        self.n = self.__p * self.__q
        self.__phi_n = (self.__p - 1) * (self.__q - 1)
        self.e = get_prime(random.randint(2, int(str(self.__phi_n)[: len(str(self.__phi_n)) // 2])))  # 随机取e，且(e, phi_n)=1
        self.__d = InvMod(self.e, self.__phi_n)[1]

    def PublicKey(self):
        """
        公钥

        :return: (e, n)
        """
        return self.e, self.n

    def PrivateKey(self):
        """
        私钥

        :return: (p, q, d, phi_n)
        """
        return self.__p, self.__q, self.__d, self.__phi_n


if __name__ == '__main__':
    # print(generate_p_q(int(input("input bit num: "))))

    rsa_key = RSA_Key(int(input("input bit num: ")))
    print(rsa_key.PublicKey())
    print(rsa_key.PrivateKey())
