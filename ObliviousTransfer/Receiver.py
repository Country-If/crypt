#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from common import *


class Receiver:
    def __init__(self, debug=False, name="Bob"):
        """
        初始化

        :param debug: bool, 是否开启调试模式
        :param name: str, 接收者名字，默认为Bob
        """
        self.debug = debug
        self.name = name
        self.n = None
        self.e = None
        self.k = None
        self.b = None
        self.X = []
        self.message_len = -1
        self.v = None
        self.message = []
        self.__result = None

    def receive_n_e(self, n, e):
        """
        接收公钥对: (n, e)

        :param n: int
        :param e: int
        """
        if self.debug:
            print(self.name + " receive (n, e): " + str((n, e)))
        self.n = n
        self.e = e

    def receive_X(self, X):
        """
        接收X列表并计算消息长度

        :param X: list, X列表
        """
        self.X = X
        if self.debug:
            print(self.name + " receive X: " + str(self.X))
        self.message_len = len(X)

    def choose_b(self, b):
        """
        选择的消息编号，下标从1开始

        :param b: int
        """
        if 1 <= b <= self.message_len:
            self.b = b - 1
        else:
            raise ValueError("b is out of range, b should be in [1, %d]" % self.message_len)

    def generate_k(self, a=100, b=1000):
        """
        生成随机数k

        :param a: int, 随机数最小值
        :param b: int, 随机数最大值
        """
        self.k = random.randint(a, b)
        if self.debug:
            print(self.name + " generate k: " + str(self.k))

    def encrypt(self):
        """
        加密：v = (X[b] + k^e) mod n
        """
        self.v = (self.X[self.b] + pow(self.k, self.e)) % self.n

    def send_v(self):
        """
        发送v值

        :return: int
        """
        if self.debug:
            print(self.name + " send v: " + str(self.v))
        return self.v

    def receive_message(self, message):
        """
        接收消息

        :param message: list, 消息列表
        """
        self.message = message
        if self.debug:
            print(self.name + " receive message: " + str(self.message))

    def decrypt(self):
        """
        解密：result = message[b] - k
        """
        self.__result = self.message[self.b] - self.k
        if self.debug:
            print(self.name + " get result: " + str(self.__result))

    def get_result(self):
        """
        获取结果

        :return: int
        """
        return self.__result

    def decrypt_all(self):
        """
        尝试解密所有消息：de[i] = message[i] - k
        """
        de = []
        for i in range(self.message_len):
            de.append(self.message[i] - self.k)
        print(self.name + " decrypt all message: " + str(de))
