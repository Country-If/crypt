#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *
from tkinter import filedialog
import tkinter as tk
import time
import os
import crypt_xor as xor


class PopUpDialog(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("输入密钥")
        self.parent = parent  # 保留父窗口
        x = parent.winfo_screenwidth() / 2 - 200
        y = parent.winfo_screenheight() / 2 - 50
        self.geometry("+%d+%d" % (x, y))        # 设置窗口位置
        self.text = StringVar()
        Entry(self, textvariable=self.text, width=60).pack(side='left')     # 文本框居左
        Button(self, text='确定', command=self.get_text).pack(side='right')   # 按钮居右

    def get_text(self):
        """
        获取文本信息
        :return: None
        """
        self.parent.key_words = self.text.get()     # 读取文本框信息
        self.destroy()      # 销毁当前窗口


class MY_GUI(tk.Tk):
    def __init__(self):
        """
        GUI窗口初始化
        """
        super().__init__()
        # self.init_window = init_window
        self.title("异或加解密")  # 窗口名
        width, height = self.maxsize()  # 获取屏幕最大值
        self.geometry("{}x{}".format(width, height))  # 窗口最大化
        # 标签
        text_width, text_height = int(width / 8), int(height / 20)
        self.preview_label = Label(self, text="文件预览")
        self.preview_label.grid(row=0)
        self.log_label = Label(self, text="日志")
        self.log_label.grid(row=text_height + 1)
        # 原始数据
        self.orig_data = ""
        # 密钥
        self.key_words = ""
        # 文本框
        self.preview_Text = Text(self, width=text_width, height=text_height)  # 文件预览结果
        self.preview_Text.grid(row=1, column=0, rowspan=text_height)
        self.log_Text = Text(self, width=text_width, height=10)  # 日志框
        self.log_Text.grid(row=text_height + 2, column=0)
        # 滚动条
        scroll_preview = Scrollbar()  # 实例化滚动条对象
        scroll_preview.grid(row=6, column=2, sticky='ns')
        scroll_preview['command'] = self.preview_Text.yview  # 将滚动条与文本框关联
        self.preview_Text.config(yscrollcommand=scroll_preview.set)  # 将滚动条填充
        scroll_log = Scrollbar()
        scroll_log.grid(row=text_height + 2, column=2, sticky='ns')
        scroll_log['command'] = self.log_Text.yview
        self.log_Text.config(yscrollcommand=scroll_log.set)
        # 按钮
        self.button_open_file = Button(self, text="打开文件", bg='lightblue', width=10,
                                       command=self.open_file)
        self.button_open_file.grid(row=1, column=text_width)
        self.button_key = Button(self, text="输入密钥", bg='lightblue', width=10,
                                 command=self.get_key)
        self.button_key.grid(row=2, column=text_width)
        self.button_encrypt = Button(self, text="加密", bg="lightblue", width=10,
                                     command=self.encrypt)
        self.button_encrypt.grid(row=3, column=text_width)
        self.button_decrypt = Button(self, text="解密", bg="lightblue", width=10,
                                     command=self.decrypt)
        self.button_decrypt.grid(row=4, column=text_width)

    def open_file(self):
        """
        读取文件
        :return: None
        """
        file = filedialog.askopenfilename(title='选择文件', initialdir=(os.path.expanduser('D:/')))  # 读取D盘文件
        self.preview_Text.delete('1.0', 'end')  # 清空文本框
        if file is not None:
            try:
                with open(file, 'rb+') as f:  # 以二进制形式读取文件
                    file_text = f.read()
                    self.orig_data = file_text
                self.preview_Text.insert('insert', file_text)  # 打印读取结果
                self.write_log_to_Text("Open File: " + str(file))  # 正常记录
                f.close()
            except FileNotFoundError:
                pass
            except Exception as e:
                self.write_log_to_Text(e)  # 异常记录

    def get_key(self):
        """
        弹出窗口获取密钥
        :return:
        """
        try:
            pw = PopUpDialog(self)      # 弹窗
            self.wait_window(pw)        # 等待
            self.write_log_to_Text("已读取密钥")
            return
        except Exception as e:
            self.write_log_to_Text(e)

    def encrypt(self):
        """加密"""
        result = xor.encrypt(self.orig_data, self.key_words)        # 加密文件
        self.preview_Text.delete('1.0', 'end')  # 清空文本框
        self.preview_Text.insert('insert', result)      # 预览结果

    def decrypt(self):
        """解密"""
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


def gui_start():
    gui = MY_GUI()  # 初始化窗口
    gui.mainloop()  # 保持窗口运行


if __name__ == "__main__":
    gui_start()
