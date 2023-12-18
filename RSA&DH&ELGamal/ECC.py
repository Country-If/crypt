#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from BaseFunction import mod_inverse


# 定义椭圆曲线类
class EllipticCurve:
    def __init__(self, a4, a6, p):
        self.a4 = a4
        self.a6 = a6
        self.p = p

    def is_on_curve(self, x, y):
        """
        判断点(x, y)是否在曲线上
        """
        return y ** 2 % self.p == (x ** 3 + self.a4 * x + self.a6) % self.p

    def add(self, P, Q):
        """
        计算P + Q
        :param P: (x1, y1)
        :param Q: (x2, y2)
        :return: (x, y)
        """
        x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
        if P == Q:
            lamb = (3 * x1 ** 2 + self.a4) * mod_inverse(2 * y1, self.p) % self.p
        else:
            lamb = (y2 - y1) * mod_inverse(x2 - x1, self.p) % self.p
        x = (lamb ** 2 - x1 - x2) % self.p
        y = (lamb * (x1 - x) - y1) % self.p
        return x, y

    def mul(self, P, n):
        """
        计算nP
        :param P: (x, y)
        :param n: int
        :return: (x, y)
        """
        if n == 1:
            return P
        elif n % 2 == 0:
            return self.mul(self.add(P, P), n // 2)
        else:
            return self.add(self.mul(self.add(P, P), n // 2), P)

    def neg(self, P):
        """
        计算P的负元
        :param P: (x, y)
        :return: (x, y)
        """
        return P[0], -P[1] % self.p


if __name__ == '__main__':
    ec = EllipticCurve(4, 20, 29)
    print(ec.is_on_curve(5, 22))
    print(ec.add((5, 22), (16, 27)))
    print(ec.mul((5, 22), 2))
    print(ec.neg((5, 22)))
