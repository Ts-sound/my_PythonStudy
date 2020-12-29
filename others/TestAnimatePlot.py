import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x, y = [], []
# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x-x))
# set x,y limit
line, = ax.plot([0, 5], [-0.030, 0.010])
ax.grid()
# line.set_xdata(x)
timeText = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def getData(Kp=8):
    x, y = [], []
    
    # 横向偏差m
    delta_d = -0.02
    delta_d_K_1 = delta_d
    # 距离目标角度偏差 rad 
    Angle = -0.017
    # PID输出角速度    rad/s
    omega = 0
    KD = 600
    # 速度m/s
    V = 0.5
    # 两点1m
    L = 5
    # 采样周期0.01s
    delta_T = 0.01

# 时间
    T = int(L / V)
    Hz = int(1 / delta_T)
    
    for i in range(0, T * Hz):
        # 记录时间 s
        x.append(i / Hz)
        # 计算当前角度
        Angle += omega * delta_T
        # 侧向偏差
        delta_d += V * delta_T * math.sin(Angle - omega * delta_T / 2)
        # 角速度
        omega = -(Kp * delta_d + KD * (delta_d - delta_d_K_1))
        # 记录数据

        y.append(delta_d)
    
        delta_d_K_1 = delta_d
    
    return x, y


def animate(i):
    # y = np.sin(x + i/100)
    x, y = getData(i / 10)
    # print(x,y)
    line.set_xdata(x)
    line.set_ydata(y)  # update the data.
    timeText.set_text('Kp =' + str(i / 10))
    return line, timeText


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=200)

# To save the animation, use e.g.
#
ani.save("movie.gif",writer= 'pillow')
#

plt.show()
