#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *


class MY_GUI:
    def __init__(self, init_window_name):
        """
        GUI窗口初始化
        :param init_window_name:
        """
        self.init_window_name = init_window_name
        self.init_window_name.title("异或加解密")  # 窗口名
        width, height = init_window_name.maxsize()  # 获取屏幕最大值
        self.init_window_name.geometry("{}x{}".format(width, height))   # 窗口最大化
        # 标签
        text_width, text_height = int(width / 8), int(height / 20)
        self.result_data_label = Label(self.init_window_name, text="文件预览")
        self.result_data_label.grid(row=0)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=text_height + 1)
        # 文本框
        self.result_data_Text = Text(self.init_window_name, width=text_width, height=text_height)  # 文件预览结果
        self.result_data_Text.grid(row=1, column=0, rowspan=text_height)
        self.log_data_Text = Text(self.init_window_name, width=text_width, height=10)  # 日志框
        self.log_data_Text.grid(row=text_height + 2, column=0)
        # 按钮
        self.button_open_file = Button(self.init_window_name, text="打开文件", bg='lightblue', width=10,
                                       command=self.open_file())
        self.button_open_file.grid(row=1, column=text_width)
        self.button_encrypt = Button(self.init_window_name, text="加密", bg="lightblue", width=10,
                                     command=self.encrypt())
        self.button_encrypt.grid(row=2, column=text_width)
        self.button_decrypt = Button(self.init_window_name, text="解密", bg="lightblue", width=10,
                                     command=self.decrypt())
        self.button_decrypt.grid(row=3, column=text_width)

    def open_file(self):
        """读取文件"""
        pass

    def encrypt(self):
        """加密"""
        pass

    def decrypt(self):
        """解密"""
        pass


def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    MY_GUI(init_window)
    init_window.mainloop()  # 保持窗口运行


if __name__ == "__main__":
    gui_start()
