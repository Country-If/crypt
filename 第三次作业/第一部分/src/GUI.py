#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *
import time
import os
from tkinter import filedialog


class MY_GUI:
    def __init__(self, init_window):
        """
        GUI窗口初始化
        :param init_window: tkinter对象
        """
        self.init_window = init_window
        self.init_window.title("异或加解密")  # 窗口名
        width, height = init_window.maxsize()  # 获取屏幕最大值
        self.init_window.geometry("{}x{}".format(width, height))  # 窗口最大化
        # 标签
        text_width, text_height = int(width / 8), int(height / 20)
        self.preview_label = Label(self.init_window, text="文件预览")
        self.preview_label.grid(row=0)
        self.log_label = Label(self.init_window, text="日志")
        self.log_label.grid(row=text_height + 1)
        # 文本框
        self.preview_Text = Text(self.init_window, width=text_width, height=text_height)  # 文件预览结果
        self.preview_Text.grid(row=1, column=0, rowspan=text_height)
        self.log_Text = Text(self.init_window, width=text_width, height=10)  # 日志框
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
        self.button_open_file = Button(self.init_window, text="打开文件", bg='lightblue', width=10,
                                       command=self.open_file)
        self.button_open_file.grid(row=1, column=text_width)
        self.button_key = Button(self.init_window, text="输入密钥", bg='lightblue', width=10,
                                 command=self.get_key)
        self.button_key.grid(row=2, column=text_width)
        self.button_encrypt = Button(self.init_window, text="加密", bg="lightblue", width=10,
                                     command=self.encrypt)
        self.button_encrypt.grid(row=3, column=text_width)
        self.button_decrypt = Button(self.init_window, text="解密", bg="lightblue", width=10,
                                     command=self.decrypt)
        self.button_decrypt.grid(row=4, column=text_width)

    def open_file(self):
        """
        读取文件
        :return: None
        """
        file = filedialog.askopenfilename(title='选择文件', initialdir=(os.path.expanduser('D:/')))     # 读取D盘文件
        self.preview_Text.delete('1.0', 'end')      # 清空文本框
        if file is not None:
            try:
                with open(file, 'rb+') as f:        # 以二进制形式读取文件
                    file_text = f.read()
                self.preview_Text.insert('insert', file_text)       # 打印读取结果
                self.write_log_to_Text("Open File: " + str(file))   # 正常记录
                f.close()
            except Exception as e:
                self.write_log_to_Text(e)   # 异常记录

    def get_key(self):
        """获取密钥"""
        pass

    def encrypt(self):
        """加密"""
        pass

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
    init_window = Tk()  # 实例化出一个父窗口
    MY_GUI(init_window)  # 设置窗口属性
    init_window.mainloop()  # 保持窗口运行


if __name__ == "__main__":
    gui_start()
