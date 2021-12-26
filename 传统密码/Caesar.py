#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Caesar:
    def __init__(self, key=3):
        self.key = key

    def encrypt(self, string):
        res = ""
        for x in string:
            if ord('A') <= ord(x) <= ord('Z'):
                if ord(x) - ord('A') + self.key >= 26:
                    res += chr(ord(x) - 26 + self.key)
                else:
                    res += chr(ord(x) + self.key)
            elif ord('a') <= ord(x) <= ord('z'):
                if ord(x) - ord('a') + self.key >= 26:
                    res += chr(ord(x) - 26 + self.key)
                else:
                    res += chr(ord(x) + self.key)
            else:
                res += x
        return res

    def decrypt(self, string):
        res = ""
        for x in string:
            if ord('A') <= ord(x) <= ord('Z'):
                if ord(x) - ord('A') - self.key < 0:
                    res += chr(ord(x) + 26 - self.key)
                else:
                    res += chr(ord(x) - self.key)
            elif ord('a') <= ord(x) <= ord('z'):
                if ord(x) - ord('a') - self.key < 0:
                    res += chr(ord(x) + 26 - self.key)
                else:
                    res += chr(ord(x) - self.key)
            else:
                res += x
        return res


if __name__ == '__main__':

    input_str = input("input string: ")
    c = Caesar()
    en_res = c.encrypt(input_str)
    print(en_res)
    de_res = c.decrypt(en_res)
    print(de_res)
