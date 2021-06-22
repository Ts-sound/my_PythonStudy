'''
Test模式下，控制器串口2上传数据处理（x，y，theta，v）

'''
import matplotlib.pyplot as plt
import re
from my_tool.my_math import hex_to_int
from my_tool.my_Exel import dataWriteToExel

#file = "C:\\Users\\76086\\Desktop\\data_12-25-1.txt"
#file = "G:\\JavaWorkspace\\Py_notes\\src\\others\\data_03-02-1.txt"
file = "data_03-02-1.txt"

xls_file = "data_03-02-1.xls"
Hz = 50

# Data 
x = []
y1, y2, y3, y4 = [], [], [], []
matrix = []

data = open(file, "r").read().replace('\n', '').replace('\r', '').replace(' ', '')

result = re.split('a0b001', data)
print(result)

matrix.append(['x','y','theta','v'])

i = 0
temp = 0
Ratio = 10000.0
for array in result:
    i += 1
    raw =[]
    if(len(array) > 31):
        # 提取0-8索引字符串，并转为int类型数据
        x.append(i / Hz)

        temp = hex_to_int(array[0:8]) / Ratio
        y1.append(temp)
        raw.append(temp)

        temp = hex_to_int(array[8:16]) / Ratio
        y2.append(temp)
        raw.append(temp)

        temp = hex_to_int(array[16:24]) / Ratio
        y3.append(temp)
        raw.append(temp)

        temp = hex_to_int(array[24:32]) / Ratio
        y4.append(temp)
        raw.append(temp)
        
        matrix.append(raw)

print(matrix)
print(y4)
dataWriteToExel(matrix,xls_file)

# 通过matplotlib画出图形
plt.figure(figsize=(14, 8), dpi=70)
#
plt.figure(1)

# ax1
ax1 = plt.subplot(221)
ax1.plot(x, y1, 'blue')
# ax1.plot(x, y2,'red')
ax1.set(xlabel='t (s)', ylabel='x(m)',
       title="")
ax1.grid()

# ax2
ax2 = plt.subplot(222)
ax2.plot(x, y2)
ax2.set(xlabel='t(s)', ylabel='v(m/s)',
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