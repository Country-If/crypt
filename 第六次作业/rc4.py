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
        R[i] = seed_key_list[k]
    # 用R表随机化S表
    j = 0
    for i in range(256):
        j = (j + S[i] + R[i]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def generate_key(S, plaintext_len):
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
        Key_Stream[i] = S[h]
    return Key_Stream


def main():
    pass


if __name__ == '__main__':
    main()
