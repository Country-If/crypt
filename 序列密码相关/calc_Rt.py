#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"


def main():
    bit_stream = input("请输入二进制串：")
    t = int(input("请输入位移值："))
    p = len(bit_stream)
    bit_shift = bit_stream[t:] + bit_stream[:t]
    print("移位后的二进制串：" + bit_shift)
    a = 0
    d = 0
    for i in range(p):
        if bit_stream[i] == bit_shift[i]:
            a += 1
        else:
            d += 1
    Rt = (a - d) / p

    print("A=" + str(a))
    print("D=" + str(d))
    print("R(t)=" + str(Rt))

    if t == 0 and Rt == 1 or 0 < t <= p - 1 and Rt == -1 / p:
        print("这个序列的自相关函数达到最佳值，具有良好的随机性")
    else:
        print("该序列未通过自相关检测")


if __name__ == '__main__':
    main()

'100110101111000'
