#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import *


def _get_prime(n):
    """
    给定整数n，获取大于等于n的素数

    :param n: int
    :return: int
    """
    while not prime_check(n):
        n += 1
    return n


class RSA:

    def __init__(self, n_bit):
        self.n_bit = n_bit
        self.__p, self.__q = generate_p_q(self.n_bit)
        self.n = self.__p * self.__q
        self.__phi_n = (self.__p - 1) * (self.__q - 1)
        # 随机选取e，满足1<e<phi_n，且(e, phi_n)=1
        self.e = _get_prime(random.randint(2, int(str(self.__phi_n)[: len(str(self.__phi_n)) // 2])))
        self.__d = InvMod(self.e, self.__phi_n)[1] % self.__phi_n

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

    def __crypt(self, a, b):
        """
        加密形如：y = a^b (mod n)

        :param a: int
        :param b: int
        :return: int
        """
        # return pow(a, b, self.n)  # 用pow()函数会快很多，官方库也是用的pow()
        return ExpMod(a, b, self.n)  # 但是作业要求是用自己写的算法...

    def encrypt(self, M):
        """
        加密运算：C = M^e (mod n)

        :param M: int
        :return: int
        """
        return self.__crypt(M, self.e)

    def decrypt(self, C):
        """
        解密运算：M = C^d (mod n)

        :param C: int
        :return: int
        """
        return self.__crypt(C, self.__d)


if __name__ == '__main__':
    # print(generate_p_q(int(input("input bit num: "))))

    rsa = RSA(int(input("input bit num: ")))
    print("(e, n)=" + str(rsa.PublicKey()))
    print("(p, q, d, phi_n)=" + str(rsa.PrivateKey()))

    m = int(input("input M: "))
    c = rsa.encrypt(m)
    print("encrypted data: " + str(c))
    m = rsa.decrypt(c)
    print("decrypted data: " + str(m))
