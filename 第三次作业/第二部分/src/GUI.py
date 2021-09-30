#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from tkinter import *
from tkinter import filedialog, messagebox
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
        self.geometry('800x400')   # 窗口大小
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
        Button(self, text="打开文件夹", bg="lightblue", width=10,
               command=self.open_directory).pack(side='right')
        Button(self, text="打开文件", bg="lightblue", width=10,
               command=self.open_file).pack(side='right')
        # 已读文件列表
        self.file_list = []

    def open_directory(self):
        """
        打开文件夹
        :return: None
        """
        directory = filedialog.askdirectory(title="选择文件夹", initialdir=(os.path.expanduser('D:/')))      # 默认打开D盘
        if directory != '':
            self.write_log_to_Text("选择文件夹：" + directory)
            self.write_log_to_Text("读取该文件夹下所有文件")
            for root, dirs, files in os.walk(directory):        # 遍历获取文件夹中所有文件
                for file in files:
                    self.file_list.append(os.path.join(root, file))
            self.write_log_to_Text("已读文件数量：" + str(len(self.file_list)))  # 日志记录
            # self.write_log_to_Text("已读文件列表：" + str(self.file_list))

    def open_file(self):
        """
        读取文件
        :return: None
        """
        try:
            file_list = filedialog.askopenfiles(title='选择文件', initialdir=(os.path.expanduser('D:/')))  # 读取D盘文件
            if len(file_list) != 0:
                try:
                    temp_file_list = []
                    for file in file_list:      # 存放每一个文件对象
                        temp_file_list.append(file)
                    print_file_list = []
                    for file in temp_file_list:     # 获取文件名列表
                        file = re.compile(r"(?<=name=\').+(?=\' mode)", re.S).findall(str(file))[0]     # 正则表达式提取文件名
                        self.file_list.append(file)
                        print_file_list.append(file)
                    self.write_log_to_Text("打开文件：" + str(print_file_list))
                    self.write_log_to_Text("已读文件数量：" + str(len(self.file_list)))
                except FileNotFoundError as e:
                    self.write_log_to_Text(e)
                except Exception as e:
                    self.write_log_to_Text(e)
        except Exception as e:      # 捕获无法打开的文件
            self.write_log_to_Text(e)
            messagebox.showerror(title="错误", message="文件无法打开")

    def button_clear(self):
        """
        清空已读文件列表
        :return: None
        """
        self.file_list = []
        self.write_log_to_Text("清空已读文件列表")

    def button_calc(self):
        """
        计算Hash值
        :return: None
        """
        if len(self.file_list) == 0:        # 判断文件列表是否为空
            messagebox.showinfo(title="提示", message="请打开文件")
        else:
            try:
                res_md5_list = []
                res_sha1_list = []
                self.write_log_to_Text("开始计算Hash值")
                # self.write_log_to_Text("计算Hash值(文件路径\t\t\tmd5\t\t\tsha1)")
                start_time = time.clock()   # 计时开始
                file_list = self.file_list.copy()       # 创建列表副本
                for file in file_list:
                    try:
                        res_md5 = md5.Hash_md5(file)        # 计算该文件的md5值
                        res_sha1 = sha1.Hash_sha1(file)     # 计算该文件的sha1值
                        # self.log_Text.insert('insert', file + '\t\t\t' + res_md5 + '\t\t\t' + res_sha1 + '\n')
                        res_md5_list.append(res_md5)
                        res_sha1_list.append(res_sha1)
                    except Exception as e:      # 捕获无法打开的文件并跳过
                        self.file_list.remove(file)     # 删除异常元素
                        self.write_log_to_Text(e)
                stop_time = time.clock()    # 计时结束
                if stop_time - start_time < 60:     # 日志记录
                    self.write_log_to_Text("计算完成，耗时 " + str(int(stop_time - start_time)) + ' s')
                else:
                    self.write_log_to_Text("计算完成，耗时 " + str(int((stop_time - start_time) / 60)) + ' min')
                # 将计算结果写入文件
                cur_path = os.getcwd()
                if not os.path.exists("../data"):  # 判断目录是否存在，不存在则创建
                    os.mkdir("../data")
                os.chdir("../data")  # 切换目录
                with open('Hash result.txt', 'w', encoding='utf-8') as f:   # 内容格式
                    f.write("文件路径\t\t\tmd5\t\t\tsha1\n\n")
                    f.close()
                for i in range(len(self.file_list)):
                    with open('Hash result.txt', 'a+', encoding='utf-8') as f:      # 以'a+'模式将结果追加到文件中
                        f.write(self.file_list[i] + '\t' + res_md5_list[i] + '\t' + res_sha1_list[i] + '\n')
                        f.close()
                self.write_log_to_Text("计算结果已写入：" + str(os.getcwd()) + "\\" + "Hash result.txt")  # 日志记录
                os.chdir(cur_path)
            except Exception as e:
                self.write_log_to_Text(e)

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
