#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


def encrypt(orig_data, key_words):
    """
    异或加密
    :param orig_data: 原始数据
    :param key_words: 密钥
    :return: str
    """
    data_len = len(orig_data)   # 获取原始数据长度
    key_len = len(key_words)    # 获取密钥长度
    key = data_len // key_len * key_words + key_words[: data_len % key_len]     # 将密钥扩展至于原始数据等长
    result = []
    for i in range(len(key)):
        result.append(chr(ord(key[i]) ^ orig_data[i]))      # 异或逐位加密
    return ''.join(result)  # 以str类型返回结果


if __name__ == '__main__':
    pass
