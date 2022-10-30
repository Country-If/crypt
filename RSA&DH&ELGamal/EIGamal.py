#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *


class EIGamal:
    def __init__(self, n_digit):
        self.p, self.g = generate_p_g(n_digit)

    def get_p_g(self):
        return self.p, self.g

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

    def encrypt(self, private_key, public_key, M):
        """
        加密算法

        :param private_key: int，自己的私钥
        :param public_key: int，对方的公钥
        :param M: int，原始数据
        :return: (int, int)，密文(C1, C2)
        """
        U = ExpMod(public_key, private_key, self.p)  # 由对方的公钥生成密钥
        C1 = ExpMod(self.g, private_key, self.p)  # 由自己的私钥生成公钥
        C2 = (U * M) % self.p  # 加密后的内容
        return C1, C2  # 发送的密文

    def decrypt(self, private_key, C):
        """
        解密算法

        :param private_key: int，自己的私钥
        :param C: (int, int)，密文(C1, C2)
        :return: int，明文
        """
        C1 = C[0]
        C2 = C[1]
        V = ExpMod(C1, private_key, self.p)
        V_inverse = ExGcd(V, self.p)[1]
        M = (C2 * V_inverse) % self.p
        return M


if __name__ == '__main__':
    n = int(input("input prime digits num: "))  # 生成大素数p的位数
    eigamal = EIGamal(n)
    print("P: " + str(eigamal.p))
    print("G: " + str(eigamal.g))
    a_private, a_public, b_private, b_public = eigamal.generate_key()  # 获取双方公钥和私钥
    print("A secret key: " + str(a_private))
    print("A public key: " + str(a_public))
    print("B secret key: " + str(b_private))
    print("B public key: " + str(b_public))
    m = int(input("input data to be encrypted: "))  # 加密数据
    A_encrypted_data = eigamal.encrypt(a_private, b_public, m)  # A加密，用A的私钥和B的公钥
    print("A encrypted result: " + str(A_encrypted_data))
    B_decrypted_data = eigamal.decrypt(b_private, A_encrypted_data)  # B解密，用B的私钥和A的密文
    print("B decrypted result: " + str(B_decrypted_data))
    B_encrypted_data = eigamal.encrypt(b_private, a_public, m)  # B加密，用B的私钥和A的公钥
    print("B encrypted result: " + str(B_encrypted_data))
    A_decrypted_data = eigamal.decrypt(a_private, B_encrypted_data)  # A解密，用A的私钥和B的密文
    print("A decrypted result: " + str(A_decrypted_data))
