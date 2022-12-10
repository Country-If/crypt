#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from common import *


class Sender:
    def __init__(self, init_len, n_bit=None, debug=False, name="Alice"):
        """
        初始化

        :param init_len: int, 消息长度
        :param n_bit: int, p * q的二进制位数，默认为随机生成
        :param debug: bool, 是否开启调试模式
        :param name: str, 发送者名字，默认为Alice
        """
        self.n = None
        self.e = None
        self.__d = None
        self.debug = debug
        self.name = name
        self.message_len = init_len
        self.__message = []
        self.X = []
        self.k = []
        self.v = None
        self.n_bit = n_bit

    def generate_n_e_d(self):
        """
        生成公钥和私钥: (n, e, d)
        """
        if self.n_bit is None:
            self.n_bit = random.randint(min_size, 20)
        self.n, self.e, self.__d = generate_RSA_key(self.n_bit)
        if self.debug:
            print(self.name + " generate (n, e, d): " + str((self.n, self.e, self.__d)))

    def get_d(self):
        """
        获取私钥

        :return: int, 私钥
        """
        return self.__d

    def generate_message(self, a=10000, b=100000):
        """
        生成消息

        :param a: int, 消息最小值
        :param b: int, 消息最大值
        """
        for i in range(self.message_len):
            self.__message.append(random.randint(a, b))
        if self.debug:
            print(self.name + " generate message: " + str(self.__message))

    def get_message(self):
        """
        获取消息

        :return: list, 消息列表
        """
        return self.__message

    def send_n_e(self):
        """
        发送公钥

        :return: tuple, 公钥对：(n, e)
        """
        if self.debug:
            print(self.name + " send (n, e): " + str((self.n, self.e)))
        return self.n, self.e

    def generate_X(self, a=100, b=1000):
        """
        生成N个随机数列表

        :param a: int, 随机数最小值
        :param b: int, 随机数最大值
        """
        for i in range(self.message_len):
            self.X.append(random.randint(a, b))

    def send_X(self):
        """
        发送随机数列表

        :return: list, 随机数列表
        """
        if self.debug:
            print(self.name + " send X: " + str(self.X))
        return self.X

    def receive_v(self, v):
        """
        接收盲化值v

        :param v: int, 盲化值
        """
        self.v = v
        if self.debug:
            print(self.name + " receive v: " + str(self.v))

    def decrypt(self):
        """
        解密X列表：k[i] = (v - X[i])^d mod n
        """
        for i in range(self.message_len):
            self.k.append(ExpMod(self.v - self.X[i], self.__d, self.n))
        if self.debug:
            print(self.name + " decrypt X: " + str(self.k))

    def encrypt(self):
        """
        加密消息：message[i] = message[i] + k[i]
        """
        for i in range(self.message_len):
            self.__message[i] += self.k[i]

    def send_message(self):
        """
        发送消息
        """
        if self.debug:
            print(self.name + " send message: " + str(self.__message))
        return self.__message
