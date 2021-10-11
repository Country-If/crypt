#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import random
from DES import *
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

if __name__ == '__main__':

    input_key = "gdut5436"
    input_data = "5436GDUT"
    orig_res = encrypt(input_data, input_key)       # 加密得到初始密文
    test_times = int(input("input test times: "))  # 测试次数
    change_data_result_list = []
    change_key_result_list = []

    # change input data
    i = 0
    while i < test_times:
        count_num_list = []
        for j in range(1, 65):
            test_data = string2bit(input_data)
            pos_list = random.sample(range(64), j)  # 改变的数据位置
            for pos in pos_list:
                # 对应位取反
                if test_data[pos] == 0:
                    test_data[pos] = 1
                else:
                    test_data[pos] = 0
            changed_res = encrypt(bit2string(test_data), input_key)  # 改变数据后加密得到的密文

            # 统计改变位数
            count_num = 0
            for t in range(64):
                if changed_res[0][t] != orig_res[0][t]:
                    count_num += 1
            count_num_list.append(count_num)

        change_data_result_list.append(count_num_list)
        i += 1

    # 绘制每次测试的图像
    plt.figure()
    for i in range(len(change_data_result_list)):
        plt.plot(range(1, 65), change_data_result_list[i])
        plt.xlabel("明文改变位数")
        plt.ylabel("输出密文位数改变情况")
        plt.title("固定密钥改变明文情况下，每次测试的密文位数改变情况")
    plt.show()
    # 绘制测试后的平均结果图像
    plt.figure()
    plt.plot(range(1, 65), np.array(change_data_result_list).mean(axis=0))
    plt.xlabel("明文改变位数")
    plt.ylabel("输出密文位数平均改变情况")
    plt.title("固定密钥改变明文情况下，测试%d次后的统计结果" % test_times)
    plt.show()

    # change input key
    i = 0
    while i < test_times:
        count_num_list = []
        for j in range(1, 65):
            test_key = string2bit(input_key)
            pos_list = random.sample(range(64), j)  # 改变的数据位置
            for pos in pos_list:
                # 对应位取反
                if test_key[pos] == 0:
                    test_key[pos] = 1
                else:
                    test_key[pos] = 0
            changed_res = encrypt(bit2string(test_key), input_key)  # 改变密钥后加密得到的密文

            # 统计改变位数
            count_num = 0
            for t in range(64):
                if changed_res[0][t] != orig_res[0][t]:
                    count_num += 1
            count_num_list.append(count_num)

        change_key_result_list.append(count_num_list)
        i += 1

    # 绘制每次测试的图像
    plt.figure()
    for i in range(len(change_key_result_list)):
        plt.plot(range(1, 65), change_key_result_list[i])
        plt.xlabel("密钥改变位数")
        plt.ylabel("输出密文位数改变情况")
        plt.title("固定明文改变密钥情况下，每次测试的密文位数改变情况")
    plt.show()
    # 绘制测试后的平均结果图像
    plt.figure()
    plt.plot(range(1, 65), np.array(change_key_result_list).mean(axis=0))
    plt.xlabel("密钥改变位数")
    plt.ylabel("输出密文位数平均改变情况")
    plt.title("固定明文改变密钥情况下，测试%d次后的统计结果" % test_times)
    plt.show()
