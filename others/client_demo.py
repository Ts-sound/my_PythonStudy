#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket               # 导入 socket 模块
import time 
from test.test_string_literals import byte

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8080))
# 接收欢迎消息:
print(s.recv(1024))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    temp = list(s.recv(1024))
    #将byte转换为int
    print(int.from_bytes(temp[0:4], byteorder='big', signed=True))

time.sleep(10)
s.send(b'exit')

while 1:
    print(list(s.recv(1024)))
s.close()