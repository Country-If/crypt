#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


def initialize_S(seed_key_list):
    """
    初始化S表

    :param seed_key_list: 种子密钥列表
    :return: 随机化处理后的S表
    """
    S = [i for i in range(256)]  # 线性填充S表
    # 用种子密钥填充R表
    R = []
    for i in range(256):
        k = i % len(seed_key_list)
        R.append(seed_key_list[k])
    # 用R表随机化S表
    j = 0
    for i in range(256):
        j = (j + S[i] + R[i]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def generate_keyStream(S, plaintext_len):
    """
    密钥流的生成

    :param S: 随机化处理后的S表
    :param plaintext_len: 明文长度
    :return: (list)密钥流
    """
    j = 0
    Key_Stream = []
    for i in range(plaintext_len):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap S[i] and S[j]
        h = (S[i] + S[j]) % 256
        Key_Stream.append(S[h])
    return Key_Stream


def crypt(text, Key_Stream):
    """
    加解密算法

    :param text: 加解密内容
    :param Key_Stream: 密钥流
    :return: (str)加解密结果
    """
    res_str = []
    for i in range(len(text)):
        res_str.append(Byte_OR(text[i], Key_Stream[i]))
    return res_str


def Byte_OR(Byte_A, Byte_B):
    """
    字节异或后返回int结果

    :param Byte_A: 字节A(整数字符)
    :param Byte_B: 字节B(整数字符)
    :return: int
    """
    res = ""
    # 转为ASCII码(str)并去掉开头的'0b'
    text_bin_str = bin(Byte_A)[2:]
    key_bin_str = bin(Byte_B)[2:]
    # 位数对齐并高位补零
    length = max(len(text_bin_str), len(key_bin_str))
    while len(text_bin_str) < length:
        text_bin_str = '0' + text_bin_str
    while len(key_bin_str) < length:
        key_bin_str = '0' + key_bin_str
    # 逐位异或
    for i in range(length):
        res += str(int(text_bin_str[i]) ^ int(key_bin_str[i]))
    return int(res, 2)  # 转为十进制数


def main():
    plaintext = input("请输入明文：")
    seed_key = input("请输入密钥：")
    # 将输入逐位转为ASCII码
    seed_key_list = []
    for string in seed_key:
        seed_key_list.append(ord(string))
    plaintext_list = []
    for string in plaintext:
        plaintext_list.append(ord(string))
    # 获取密钥流以及加解密
    KeyStream = generate_keyStream(initialize_S(seed_key_list), len(plaintext))
    en_res = crypt(plaintext_list, KeyStream)
    de_res = crypt(en_res, KeyStream)
    # 打印输出结果
    print("密钥流：" + str(KeyStream))
    print("明文对应ASCII值列表：" + str(plaintext_list))
    print("加密后密文对应ASCII值列表：" + str(en_res))
    print("解密后结果对应ASCII值列表：" + str(de_res))


if __name__ == '__main__':
    main()
