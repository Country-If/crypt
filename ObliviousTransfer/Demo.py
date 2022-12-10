#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Maylon"

from Sender import Sender
from Receiver import Receiver
from random import randint

if __name__ == '__main__':
    sender = Sender(randint(6, 10), debug=True)  # <--- 参数可调
    receiver = Receiver(debug=True)

    sender.generate_message()  # <--- 参数可调

    sender.generate_n_e_d()
    n, e = sender.send_n_e()
    receiver.receive_n_e(n, e)

    sender.generate_X()  # <--- 参数可调
    X = sender.send_X()
    receiver.receive_X(X)

    receiver.generate_k()  # <--- 参数可调
    receiver.choose_b(int(input("Please choose num(b): ")))

    receiver.encrypt()
    v = receiver.send_v()
    sender.receive_v(v)

    sender.decrypt()
    sender.encrypt()

    message = sender.send_message()
    receiver.receive_message(message)

    receiver.decrypt()

    print()
    receiver.decrypt_all()
