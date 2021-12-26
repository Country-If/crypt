#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import math
from collections import OrderedDict

# 字母表
_square = (
    u"A", u"B", u"C", u"D", u"E",
    u"F", u"G", u"H", u"IJ", u"K",
    u"L", u"M", u"N", u"O", u"P",
    u"Q", u"R", u"S", u"T", u"U",
    u"V", u"W", u"X", u"Y", u"Z",
)
# 插入字母
_insert_char = 'X'


# 密码表
class _Square:

    def __init__(self, key=None):
        self.__side = int(math.ceil(math.sqrt(len(_square))))
        if key:  # 关键词构造字母矩阵
            key = _Data_check(key)
            indexes = {c: i for i, letters in enumerate(_square) for c in letters}
            # 去掉重复字母
            key_i = OrderedDict.fromkeys(indexes[char] for char in key)
            self.__alphabet = [_square[i] for i in key_i]

            for i, a in enumerate(_square):
                if i not in key_i:
                    self.__alphabet.append(a)
        else:
            self.__alphabet = _square
        self.coords = {c: divmod(i, self.__side) for i, letters in enumerate(self.__alphabet) for c in letters}

    def get_coordinates(self, char):
        return self.coords[char]

    def get_char(self, row, column):
        return self.__alphabet[row * self.__side + column][0]


# 过滤非字母数据并返回大写字母，返回字符串
def _Data_check(string):
    res = ''
    err = 0
    for x in string:
        if ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z'):  # 判断是否是字母
            res += x.upper()
        else:
            err = 1
    if err == 1:
        raise ValueError("Encrypt letters only")
    return res


# 数据分组处理，返回列表
def _Prepare_text(string):
    txt = []
    i = 1
    while i < len(string):
        txt.append(string[i - 1])
        if string[i - 1] == string[i]:  # 判断分组是否有重复字母
            txt.append(_insert_char)
            i += 1
        else:
            txt.append(string[i])
            i += 2
    if i == len(string):  # 判断最后一个分组是否只有一个字母
        txt.append(string[i - 1])
        txt.append(_insert_char)
    return txt


# playfair核心算法：对两个字母进行加密
def _crypt(a, b, square, adjustment):
    cols = 5
    rows = 5
    # 获取字母a、b坐标
    a_row, a_column = square.get_coordinates(a)
    b_row, b_column = square.get_coordinates(b)
    # 加密得到密文坐标
    if a_row == b_row:
        a_column = (a_column + adjustment) % cols
        b_column = (b_column + adjustment) % cols
    elif a_column == b_column:
        a_row += adjustment
        b_row += adjustment
        if a_row >= rows:
            a_row = 0
        if b_row >= rows:
            b_row = 0
    else:
        a_column, b_column = b_column, a_column
    # 根据密文坐标获取密文
    a = square.get_char(a_row, a_column)
    b = square.get_char(b_row, b_column)
    return a + b


class Playfair:
    def __init__(self, key):
        self.square = _Square(key)

    # 加密函数
    def encrypt(self, text):
        txt = _Prepare_text(_Data_check(text))  # 获取分组后的明文
        return "".join(_crypt(txt[i - 1], txt[i], self.square, 1) for i in range(1, len(txt), 2))  # 分组加密

    # 解密函数
    def decrypt(self, text):
        res = [_crypt(text[i - 1], text[i], self.square, -1) for i in range(1, len(text), 2)]  # 分组解密
        # 去掉增加的字母
        for i in range(1, len(res)):
            if res[i - 1][0] == res[i][0] and res[i - 1][1] == _insert_char:
                res[i - 1] = res[i - 1][0]
        # 检查最后一个字母
        if res and res[-1][1] == _insert_char:
            res[-1] = res[-1][0]

        return "".join(res)


if __name__ == '__main__':

    input_string = input("input string: ")
    p = Playfair(input_string)
    encrypt_res = p.encrypt(input_string)
    print(encrypt_res)
    decrypt_res = p.decrypt(encrypt_res)
    print(decrypt_res)
