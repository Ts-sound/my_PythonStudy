'''
client_agv
接收AGV的实时位置数据信息，并用matplotlib画图
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import socket               # 导入 socket 模块
import time
import re
import math
import xlwt
#定义AGV小车ip地址及端口
#测试    '127.0.0.1'    8080
#实际    '192.168.43.101'    4002
#host = '127.0.0.1'
#port =  8080
host = '192.168.43.101'
port = 4002
#记录数据时间
Time = 50
#存储数据文件
file_name = 'data_12-25-2.txt'
#数据上传频率 
Hz = 50
outData_excel = []
file_excel = 'data.xls'

#将补码数据转换为int类型数据
def byte32ToInt(byte32):
    if(byte32&0x80000000 == 0):
        r = byte32
    else:
        byte32 = byte32^0xFFFFFFFF
        byte32 = byte32 + 1
        r = -byte32
    return r


#通过plt画图
# t, x,y,theta,omega (s\m\°)
def flt_figure(x,y1,y2,y3,y4):
    # 通过matplotlib画出图形
    plt.figure(figsize=(14, 8), dpi=70)
    #
    plt.figure(1)
    
    # ax1
    ax1 = plt.subplot(221)
    ax1.plot(x, y1, 'blue')
    ax1.set(xlabel='t (s)', ylabel='x(mm)',
            title="")
    ax1.grid()
    
    # ax2
    ax2 = plt.subplot(222)
    ax2.plot(x, y2)
    ax2.set(xlabel='t(s)', ylabel='y(mm)',
       title='')
    ax2.grid()
    
    # ax3
    ax3 = plt.subplot(223)
    ax3.plot(x, y3)
    ax3.set(xlabel='t(s)', ylabel='theta(°)',
       title='')
    ax3.grid()

    # ax3
    ax4 = plt.subplot(224)
    ax4.plot(x, y4)
    ax4.set(xlabel='t(s)', ylabel='omega(rad/s)',
            title='')
    ax4.grid()
    #
    plt.figure(1)

    #
    plt.tight_layout()
    #plt.savefig("figure.png")
    plt.show()


#数据处理
def data_analysis(data):
    x = []
    y1, y2, y3,y4 = [], [], [], []
    i = 0
    result = re.split('a0b001', data)
    #print(result)
    
    for array in result:
        i += 1
        data_t = []
        if(len(array) > 24):
            #提取0-8索引字符串，并转为int类型数据
            x.append(i/Hz)
            temp = byte32ToInt(int(array[0:8],16))/10000
            y1.append(temp)
            data_t.append(temp)
            temp = byte32ToInt(int(array[8:16],16))/10000
            y2.append(temp)
            data_t.append(temp)
            temp = byte32ToInt(int(array[16:24],16))/10000
            y3.append(temp)
            data_t.append(temp)
            temp = byte32ToInt(int(array[24:32],16))/10000
            y4.append(temp)
            data_t.append(temp)
            
            outData_excel.append(data_t)
            
    print(y1)      


    flt_figure(x,y1,y2,y3,y4)
    
def dataWriteToExel(matrix=[[]],fileName = 'null.xls'):
    
    xl = xlwt.Workbook(encoding='utf-8');

    sheet1 = xl.add_sheet('data1')

 
    # write matrix data 
    for row in range(0,len(matrix)):
        for colunm in range(0,len(matrix[row])):
#             print(colunm)
#             print(matrix[row][colunm])
            sheet1.write(row, colunm, matrix[row][colunm])

    
    xl.save(fileName)
#创建存储文件

# 
f = open(file_name,'a')    #存储数据文件
a = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect((host, port))

star_time =  time.time()
print(star_time)

cur_time = star_time

i = 0

while(cur_time < (star_time + Time)): 
    cur_time = time.time()
    temp = s.recv(1024)
    a += bytearray(temp).hex()
    i +=1
    print(cur_time)

print(cur_time)
print(i)

s.close()
    
data_analysis(a)
f.write(a)
dataWriteToExel(outData_excel,file_excel)

