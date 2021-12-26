#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy as np
import string
import math

str_dict = {s: ord(s) - ord('A') for s in list(string.ascii_uppercase)}
num_dict = {ord(s) - ord('A'): s for s in list(string.ascii_uppercase)}
mod_dict = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}  # 模26倒数表


# 求矩阵的行列式
def _det_calculation(arr):
    if arr.shape[0] == 1:
        return arr[0][0]
    S = 0
    for i in range(arr.shape[0]):
        arr1 = np.delete(arr, 0, 0)  # delete first row
        arr1 = np.delete(arr1, i, 1)  # delete ith column
        S += (-1) ** (1 + i + 1) * arr[0, i] * _det_calculation(arr1)  # Laplace formula
    return S


# 字符串转为数字列表
def _String_To_NumList(String):
    res = []
    for x in String:
        res.append(str_dict[x])
    return res


# 数字列表转为字符串
def _NumList_To_String(num_list):
    res = ""
    for num in num_list:
        res += num_dict[num]
    return res


# Hill核心算法：对m个字母进行加密
def _crypt(String, key):
    P = np.array(_String_To_NumList(String))
    dot_res = np.dot(key, P)
    num_list = []
    for i in range(len(dot_res)):
        num_list.append(math.ceil(dot_res[i]) % 26)

    return _NumList_To_String(num_list)


class Hill:
    def __init__(self, m=3, insert_char='V', key_start=10, key_end=50):
        self.m = m
        self.insert_char = insert_char
        self.key_start = key_start
        self.key_end = key_end
        self.__key = self.__Create_key_matrix()  # 默认生成整数范围在[10, 50)的m阶矩阵
        self.__inverse_key = self.__Inverse_matrix(self.__key)

    # 创建随机密钥矩阵
    def __Create_key_matrix(self):
        arr = np.random.randint(self.key_start, self.key_end, size=(self.m, self.m))
        if _det_calculation(arr) % 26 in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:  # 判断矩阵是否摸26可逆
            return arr  # 返回矩阵
        else:
            return self.__Create_key_matrix()

    # 求模26可逆矩阵
    def __Inverse_matrix(self, matrix):
        A = np.zeros((self.m, self.m))
        for i in range(self.m):
            for j in range(self.m):
                # 代数余子式模26
                A[i][j] = pow(-1, i + j) * _det_calculation(np.delete(np.delete(matrix, i, axis=0), j, axis=1)) % 26
        det = mod_dict[math.ceil(_det_calculation(matrix) % 26)]
        return (A * det % 26).T

    # 数据分组处理，返回分组列表
    def __Pre_handle_data(self, String):
        String = String.upper()
        for x in String:
            if not ord('A') <= ord(x) <= ord('Z'):
                raise ValueError("Encrypt letters only")
        res = []
        i = 0
        while i < len(String):
            tmp = ""
            tmp += String[i]
            for j in range(1, self.m):
                if i + j < len(String):  # 分组后长度不足m时补字母
                    tmp += String[i + j]
                else:
                    tmp += self.insert_char
            res.append(tmp)
            i += self.m
        return res

    # 加密函数
    def encrypt(self, String):
        key = self.__key  # 加密密钥
        pre_list = self.__Pre_handle_data(String)
        res = ""
        for data in pre_list:  # 分组加密
            res += _crypt(data, key)
        return res

    # 解密函数
    def decrypt(self, String):
        key = self.__inverse_key  # 解密密钥
        pre_list = self.__Pre_handle_data(String)
        res = ""
        for data in pre_list:  # 分组解密
            res += _crypt(data, key)
        # 删除添加的字符
        while res and res[-1] == self.insert_char:
            res = res[: -1]
        return res


if __name__ == '__main__':
    input_data = input("input string: ")
    h = Hill()
    en_res = h.encrypt(input_data)
    de_res = h.decrypt(en_res)
    print(en_res)
    print(de_res)
