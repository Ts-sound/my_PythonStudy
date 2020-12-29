import numpy as np
import matplotlib.pyplot as plt
import xlrd

xl = xlrd.open_workbook(r'G:\1.xlsx')
table = xl.sheets()[0]
print(table)

col0 = table.col_values(0)
col1 = table.col_values(1)
print(col0)
print(col1)

# Data for plotting
x,x2 = [],[]
y1,y2 = [],[]

angle = [0.017]
omega = [0]
Angle_cur = 0
omega = 0

kp = 1
kd = 1
#s
delta_T = 0.01

#1s,10ms
Hz = int(1/delta_T);
for i in range(0, Hz):
    x.append(i/Hz)
    y1.append(i*i)
    y2.append(col1[i + 1])

#
plt.figure(figsize=(8,8),dpi=70)
#
plt.figure(1)
#
ax1 = plt.subplot(211)
ax1.plot(x, y1,'blue')
ax1.plot(x, y2,'red')

ax1.set(xlabel='t (s)', ylabel='angle (deg)',
       title='car_angle')
#
ax2 = plt.subplot(212)
ax2.plot(x, y2)
#ax2.set(xlim=[0.5, 4.5], ylim=[-2, 8],xlabel='t(s)', ylabel='angle (deg)',title='Figure2')
ax2.grid()

#
#plt.figure(2)
#x = np.arange(4)
#y = np.array([15,20,18,25])
#plt.bar(x,y)
#plt.title("bar")

#
plt.figure(1)


#
plt.tight_layout()
plt.show()