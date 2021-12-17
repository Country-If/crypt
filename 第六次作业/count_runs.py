#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from collections import Counter


def count(bit_stream, bit_count):
    """
    统计0或1连续出现的次数

    :param bit_stream: 比特流
    :param bit_count: 0/1
    :return: list
    """
    count_list = []
    count_num = 0
    for bit in bit_stream:
        if bit == str(bit_count):
            count_num += 1
        else:
            if count_num != 0:
                count_list.append(count_num)
            count_num = 0
    # 处理漏网之鱼
    if count_num != 0:
        count_list.append(count_num)
    return count_list


def main():
    bit_stream = input("请输入二进制串：")
    # 统计0游程和1游程的个数
    one = count(bit_stream, 1)
    zero = count(bit_stream, 0)
    runs_sum = 0
    # 打印结果
    for key, value in dict(Counter(one)).items():
        runs_sum += value
        print("长度为" + str(key) + "的1游程的个数：" + str(value))
    for key, value in dict(Counter(zero)).items():
        runs_sum += value
        print("长度为" + str(key) + "的0游程的个数：" + str(value))
    print("游程总数为：" + str(runs_sum))


if __name__ == '__main__':
    main()

'100110101111000'
