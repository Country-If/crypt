#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
import time
import re
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
        Button(self, text="清空文件列表", bg="lightblue", width=10,
               command=self.button_clear).pack(side='right')
        Button(self, text="打开文件", bg="lightblue", width=10,
               command=self.open_file).pack(side='right')
        # 已读文件列表
        self.file_list = []

    def open_file(self):
        """
        读取文件
        :return: None
        """
        try:
            file_list = filedialog.askopenfiles(title='选择文件', initialdir=(os.path.expanduser('D:/')))   # 读取D盘文件
            temp_file_list = []
            for file in file_list:      # 存放每一个文件对象
                temp_file_list.append(file)
            for file in temp_file_list:     # 获取文件名列表
                file = re.compile(r"(?<=name=\').+(?=\' mode)", re.S).findall(str(file))[0]     # 正则表达式提取文件名
                self.file_list.append(file)
            self.write_log_to_Text("已读文件列表：" + str(self.file_list))     # 日志记录
        except FileNotFoundError as e:
            self.write_log_to_Text(e)
        except Exception as e:
            self.write_log_to_Text(e)

    def button_clear(self):
        self.file_list = []
        self.write_log_to_Text("清空已读文件列表")

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
