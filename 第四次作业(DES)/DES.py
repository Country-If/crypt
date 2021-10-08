#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


def string2bit(str_data):
    """
    将字符串数据转换为比特位列表
    :param str_data: string
    :return: list of bits (0,1)'s
    """
    data = [ord(c) for c in str_data]
    L = len(data) * 8
    result = [0] * L
    pos = 0
    for ch in data:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result


def bit2string(bit_data):
    """
    将位数据转换为字符串数据
    :param bit_data: bit list
    :return: string
    """
    result = []
    pos = 0
    c = 0
    while pos < len(bit_data):
        c += bit_data[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1

    return ''.join([chr(c) for c in result])
    # return bytes(result)


if __name__ == '__main__':
    bit_res = string2bit(input("input string: "))
    str_res = bit2string(bit_res)
    print(str_res)
