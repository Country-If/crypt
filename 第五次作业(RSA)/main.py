#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import sys
from RSA import *
from EIGamal import *
from DH import *


def menu():
    choice = int(input("0.退出\t1.RSA\t2.EIGamal\t3.DH\n"))
    if choice == 0:
        sys.exit(0)
    elif choice == 1:
        try:
            rsa = RSA(int(input("input bit num: ")))
            print("(e, n)=" + str(rsa.PublicKey()))
            print("(p, q, d, phi_n)=" + str(rsa.PrivateKey()))

            m = int(input("input M: "))
            c = rsa.encrypt(m)
            print("encrypted data: " + str(c))
            m = rsa.decrypt(c)
            print("decrypted data: " + str(m))
        except Exception as e:
            print("Error: " + str(e))
        menu()
    elif choice == 2:
        try:
            n = int(input("input prime digits num: "))  # 生成大素数p的位数
            eigamal = EIGamal(n)
            a_private, a_public, b_private, b_public = eigamal.generate_key()  # 获取双方公钥和私钥
            print("A private key: " + str(a_private))
            print("A public key: " + str(a_public))
            print("B private key: " + str(b_private))
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
        except Exception as e:
            print("Error: " + str(e))
        menu()
    elif choice == 3:
        try:
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
        except Exception as e:
            print("Error: " + str(e))
        menu()
    else:
        print("Wrong input, try again.")
        menu()


if __name__ == '__main__':
    menu()
