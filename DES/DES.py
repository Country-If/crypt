#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

# macro definition
_ENCRYPT = 0x00
_DECRYPT = 0x01
_block_size = 64
_key_size = 64


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


def _permutate(table, block):
    """
    根据指定顺序置换数据

    :param table: permutate list
    :param block: bit list
    :return: list
    """
    return list(map(lambda x: block[x], table))


def _create_sub_keys(key):
    """
    创建子密钥

    :param key: bit list
    :return: list of sub_key lists
    """
    # 初始置换
    key = _permutate(_pc1, key)
    i = 0
    # 切分密钥
    L = key[:28]
    R = key[28:]
    Kn = [[0] * 48] * 16
    while i < 16:
        j = 0
        # 根据左移次数列表 循环左移
        while j < _left_rotations[i]:
            L.append(L[0])
            del L[0]
            R.append(R[0])
            del R[0]
            j += 1
        # 通过pc2 创建子密钥
        Kn[i] = _permutate(_pc2, L + R)
        i += 1
    return Kn


def des_crypt(block, Kn, crypt_type):
    """
    DES核心算法

    :param block: bit list
    :param Kn: sub keys
    :param crypt_type: ENCRYPT / DECRYPT
    :return: bit list
    """
    # 初始置换
    block = _permutate(_ip, block)
    L = block[:32]
    R = block[32:]

    # 加密从Kn[1]到Kn[16] (下标从0开始)
    if crypt_type == _ENCRYPT:
        iteration = 0
        iteration_adjustment = 1
    # 解密从Kn[16]到Kn[1]
    else:
        iteration = 15
        iteration_adjustment = -1

    i = 0
    while i < 16:
        # 复制R[i-1]，将会变成L[i]
        tempR = R[:]

        # 选择运算E
        R = _permutate(_expansion_table, R)

        # 中间结果与子密钥相异或，切分为8块
        R = list(map(lambda x, y: x ^ y, R, Kn[iteration]))
        B = [R[:6], R[6:12], R[12:18], R[18:24],
             R[24:30], R[30:36], R[36:42], R[42:]]

        # 代替函数组S
        j = 0
        Bn = [0] * 32
        pos = 0
        while j < 8:
            # 计算偏移量
            m = (B[j][0] << 1) + B[j][5]  # 行号
            n = (B[j][1] << 3) + (B[j][2] << 2) + (B[j][3] << 1) + B[j][4]  # 列号

            # 求排列值(S盒的输出值)
            v = _S_box[j][(m << 4) + n]

            # 将值转换为位，写入Bn
            Bn[pos] = (v & 8) >> 3
            Bn[pos + 1] = (v & 4) >> 2
            Bn[pos + 2] = (v & 2) >> 1
            Bn[pos + 3] = v & 1

            pos += 4
            j += 1

        # 置换运算P
        R = _permutate(_p, Bn)

        R = list(map(lambda x, y: x ^ y, R, L))

        # L[i] = R[i - 1]
        L = tempR

        i += 1
        iteration += iteration_adjustment

    # 逆初始置换IP^-1 (R在左 L在右)
    final = _permutate(_fp, R + L)
    return final


def _check_key(key):
    """
    检查密钥是否符合规范

    :param key: string
    :return: bit list
    """
    key = string2bit(key)
    key_len = len(key)
    if key_len % _key_size != 0:
        for i in range(_key_size - (key_len % _key_size)):
            key.append(0)  # 不够位数补0
    return key


def _check_data(data):
    """
    检查数据是否符合规范

    :param data: string
    :return: list of block lists
    """
    data = string2bit(data)
    data_len = len(data)

    if data_len % _block_size != 0:
        for i in range(_block_size - (data_len % _block_size)):
            data.append(0)  # 不够位数补0

    data_len = len(data)
    res = []
    i = 0
    # 将数据切块
    while i < data_len - 1:
        res.append(data[i: i + _block_size])
        i += _block_size
    return res


def encrypt(data, key):
    """
    加密功能

    :param data: string
    :param key: string
    :return: list of bit lists
    """
    data_list = _check_data(data)
    Kn = _create_sub_keys(_check_key(key))
    res = []
    for data in data_list:  # 逐块加密
        res.append(des_crypt(data, Kn, _ENCRYPT))
    return res


def decrypt(block_list, key):
    """
    解密功能

    :param block_list: list of bit lists
    :param key: string
    :return: list of bit lists
    """
    Kn = _create_sub_keys(_check_key(key))
    res = []
    for block in block_list:    # 逐块解密
        res.append(des_crypt(block, Kn, _DECRYPT))
    return res


# Permutation and translation tables for DES (8 * 7)
_pc1 = [56, 48, 40, 32, 24, 16, 8,
        0, 57, 49, 41, 33, 25, 17,
        9, 1, 58, 50, 42, 34, 26,
        18, 10, 2, 59, 51, 43, 35,
        62, 54, 46, 38, 30, 22, 14,
        6, 61, 53, 45, 37, 29, 21,
        13, 5, 60, 52, 44, 36, 28,
        20, 12, 4, 27, 19, 11, 3
        ]

# number left rotations of pc1 (1 * 16)
_left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# permuted choice key (table 2) (8 * 6)
_pc2 = [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]

# initial permutation IP (8 * 8)
_ip = [57, 49, 41, 33, 25, 17, 9, 1,
       59, 51, 43, 35, 27, 19, 11, 3,
       61, 53, 45, 37, 29, 21, 13, 5,
       63, 55, 47, 39, 31, 23, 15, 7,
       56, 48, 40, 32, 24, 16, 8, 0,
       58, 50, 42, 34, 26, 18, 10, 2,
       60, 52, 44, 36, 28, 20, 12, 4,
       62, 54, 46, 38, 30, 22, 14, 6
       ]

# Expansion table for turning 32 bit blocks into 48 bits (8 * 6)
_expansion_table = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]

# The (in)famous S-boxes [(4 * 16) * 8]
_S_box = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]

# 32-bit permutation function P used on the output of the S-boxes (6 * 6)
_p = [
    15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17, 30, 9, 1, 7,
    23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10,
    3, 24
]

# final permutation IP^-1 (8 * 8)
_fp = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]

if __name__ == '__main__':

    input_key = input('input key: ')
    input_data = input('input data: ')
    print("input data: ")
    print(_check_data(input_data))
    encrypt_result = encrypt(input_data, input_key)
    print("encrypt result: ")
    print(encrypt_result)
    print("".join([bit2string(block) for block in encrypt_result]))
    decrypt_result = decrypt(encrypt_result, input_key)
    print("decrypt result: ")
    print(decrypt_result)
