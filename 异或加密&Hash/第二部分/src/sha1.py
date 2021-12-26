#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

import hashlib


def Hash_sha1(file_path, Bytes=1024):
    """
    计算文件的哈希值(sha1算法)
    :param file_path: 文件路径
    :param Bytes: 读取字节数
    :return: str
    """
    sha1 = hashlib.sha1()  # 创建一个sha1算法对象
    with open(file_path, 'rb') as f:  # 打开文件
        while True:
            data = f.read(Bytes)  # 每次只读取固定字节
            if data:  # 当读取内容不为空时对读取内容进行更新
                sha1.update(data)
            else:  # 当整个文件读完之后停止更新
                break
    res = sha1.hexdigest()  # 获取这个文件的sha1值(十六进制)
    return res


if __name__ == '__main__':
    print(Hash_sha1('./sha1.py'))
