# -- coding: utf-8 --
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import time 
'''
运动导航控制仿真-PID
'''

# Data for plotting
x = []
y1, y2, y3 = [], [], []

# 横向偏差m
delta_d = -0.02
delta_d_K_1 = delta_d
# 距离目标角度偏差 rad 
Angle = -0.017
# PID输出角速度    rad/s
omega = 0
KP = 8
KD = 600
# 速度m/s
V = 0.5
#两点1m
L = 5
# 采样周期0.01s
delta_T = 0.01

# 时间
T = int(L/V)
Hz = int(1 / delta_T)

for i in range(0, T * Hz):
    # 记录时间 s
    x.append(i / Hz)
    # 计算当前角度
    Angle += omega * delta_T
    # 侧向偏差
    delta_d += V * delta_T * math.sin(Angle - omega * delta_T / 2)
    # 角速度
    omega = -(KP * delta_d + KD * (delta_d - delta_d_K_1))
    # 记录数据
    y1.append(Angle * 180 / math.pi)
    y2.append(omega * 180 / math.pi)
    y3.append(delta_d)
    
    delta_d_K_1 = delta_d
    

# 通过matplotlib画出图形
plt.figure(figsize=(14, 8), dpi=70)
#
plt.figure(1)

# ax1
ax1 = plt.subplot(221)
line1, = ax1.plot([0,10], [-20,20], 'blue')
line1.set_xdata(x)
line1.set_ydata(y2)
# ax1.plot(x, y2,'red')
ax1.set(xlabel='t (s)', ylabel='angle (°)',
       title="angle")
ax1.grid()

# ax2
ax2 = plt.subplot(222)
ax2.plot(x, y2)
ax2.set(xlabel='t(s)', ylabel='omega (°/s)',
       title='omega')
ax2.grid()

# ax3
ax3 = plt.subplot(223)
ax3.plot(x, y3)
ax3.set(xlabel='t(s)', ylabel='d (m)',
       title='delta_d')
ax3.grid()

#
plt.tight_layout()

def animate(i):
    y = np.sin(x + i/100)
    line1.set_ydata(y)  # update the data.
    return line1,

ax1.plot (x,y1)
time.sleep(1)
ax1.plot (x,y2)
time.sleep(1)
ax1.plot (x,y3)
time.sleep(1)

plt.show()

# ani = animation.FuncAnimation(
#     fig, animate, interval=20, blit=True, save_count=50)