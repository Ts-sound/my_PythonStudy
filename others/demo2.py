# -- coding: utf-8 --
import matplotlib.pyplot as plt

'''
通过PID调节角速度，控制角度到达目标角度
'''

# Data for plotting
x = []
y1,y2 = [],[]

#距离目标角度偏差 rad
Angle_pre = 0.017
Angle_cur = 0
#PID输出角速度    rad/s
omega = 0

#pid参数
kp = 10
kd = 1

#0.01s调整一次
delta_T = 0.01

#1s
Hz = int(1/delta_T)

for i in range(0, Hz):
    #记录时间 s
    x.append(i/Hz)
    #计算当前角度
    Angle_cur = Angle_pre - omega * delta_T
    #PID输出角速度
    omega = kp * Angle_cur + kd*(Angle_cur-Angle_pre)
    #记录数据
    y1.append(Angle_cur)
    y2.append(omega)
    #当前角度值给前一角度值
    Angle_pre = Angle_cur


#通过matplotlib画出图形
plt.figure(figsize=(12,8),dpi=70)
#
plt.figure(1)
#
ax1 = plt.subplot(211)
ax1.plot(x, y1,'blue')
#ax1.plot(x, y2,'red')
ax1.grid()

ax1.set(xlabel='t (s)', ylabel='angle (rad)',
       title="angle")
#
ax2 = plt.subplot(212)
ax2.plot(x, y2)
ax2.set(xlabel='t(s)', ylabel='omega (rad/s)',
       title='omega')
ax2.grid()

#
#plt.figure(2)
#x = np.arange(4)
#y = np.array([15,20,18,25])
#plt.bar(x,y)
#plt.title("bar")

#
plt.figure(1)

line, = ax1.plot(x, y1)

plt.tight_layout()
plt.show()