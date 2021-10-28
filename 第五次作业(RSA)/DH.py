#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *


class DH:
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
        B_public = ExpMod(self.g, B_private, self.p)
        # A_public = pow(self.g, A_private, self.p)  # 速度慢时用pow()函数提高效率
        # B_public = pow(self.g, B_private, self.p)
        return A_private, A_public, B_private, B_public

    def get_secret_key(self, public_key, private_key):
        """
        计算密钥

        :param public_key: int，公钥
        :param private_key: int，私钥
        :return: int，密钥
        """
        return ExpMod(public_key, private_key, self.p)
        # return pow(public_key, private_key, self.p)  # 速度慢时用pow函数


if __name__ == '__main__':
    n = int(input("input prime digits num: "))  # 生成大素数p的位数
    dh = DH(n)
    a_private, a_public, b_private, b_public = dh.generate_key()  # 获取双方公钥和私钥
    print("A private key: " + str(a_private))
    print("A public key: " + str(a_public))
    print("B private key: " + str(b_private))
    print("B public key: " + str(b_public))
    A_secret_key = dh.get_secret_key(b_public, a_private)
    B_secret_key = dh.get_secret_key(a_public, b_private)
    print("A secret key: " + str(A_secret_key))
    print("B secret key: " + str(B_secret_key))
