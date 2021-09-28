#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *
import tkinter as tk
import os
import time
import md5
import sha1


class MY_GUI(tk.Tk):
    def __init__(self):
        """
        GUI窗口初始化
        """
        super().__init__()
        self.title("计算磁盘文件Hash值")  # 窗口名
        # 标签
        Label(self, text="日志").pack(side='top')
        # 文本框
        self.log_Text = Text(self)
        self.log_Text.pack(fill='x')
        # 按钮
        Button(self, text="计算Hash值", bg="lightblue", width=10,
               command=self.button_calc).pack(side='right')
        Button(self, text="打开文件", bg="lightblue", width=10,
               command=self.open_file).pack(side='right')

    def open_file(self):
        pass

    def button_calc(self):
        pass

    def write_log_to_Text(self, log_msg):
        """
        日志动态打印
        :param log_msg: 日志信息
        :return: None
        """
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        log_msg_in = str(current_time) + " " + str(log_msg) + "\n"  # 日志信息
        self.log_Text.insert(END, log_msg_in)  # 插入日志信息并换行


def main():
    gui = MY_GUI()  # 初始化窗口
    gui.mainloop()  # 保持窗口运行


if __name__ == '__main__':
    main()
