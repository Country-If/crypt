#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
from Caesar import *
from Playfair import *
from Hill import *


def menu():
    choice = int(input("1.Caesar密码 \t2.Playfair密码 \t3.Hill密码 \t4.退出\n"))
    if choice == 1:
        try:
            get_input = input("请输入偏移值(不输入则以3作为偏移值)：")
            k = 3 if not get_input else int(get_input)
            data = input("请输入加密内容：")
            C = Caesar(k)
            e = C.encrypt(data)
            print("加密结果：" + e)
            d = C.decrypt(e)
            print("解密结果：" + d)
        except Exception as e:
            print("Error: " + str(e))
        menu()
    elif choice == 2:
        try:
            k = input("请输入密钥(不输入则以加密内容作为密钥)：")
            data = input("请输入加密内容：")
            P = Playfair(k)
            e = P.encrypt(data)
            print("加密结果：" + e)
            d = P.decrypt(e)
            print("解密结果：" + d)
        except Exception as e:
            print("Error: " + str(e))
        menu()
    elif choice == 3:
        try:
            get_input = input("请输入m值(不输入则以3作为m值)：")
            k = 3 if not get_input else int(get_input)
            data = input("请输入加密内容：")
            H = Hill(k)
            e = H.encrypt(data)
            print("加密结果：" + e)
            d = H.decrypt(e)
            print("解密结果：" + d)
        except Exception as e:
            print("Error: " + str(e))
        menu()
    elif choice == 4:
        sys.exit(0)
    else:
        print("请重新输入")
        menu()


if __name__ == '__main__':
    menu()
