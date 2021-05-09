from my_CarMoveModel.Car import MyCarClass
from my_CarMoveModel.my_DrawCarPos import drawCarPos
import numpy as np
import math 
'''
x,y,theta,
 m , m , ° 
'''
# 起点位姿[x,y,thta]
startPos = [0.0, 0.0, 0.0,0,0]
prePos = startPos
curPos = startPos
v = 0.5   # m/s

# 目标点位姿
tar_x = 2.0
tar_y = 2.0
tar_theta = 45
targetPos = [tar_x, tar_y, tar_theta]

#权重，kp、kd系数
WeightX = -math.sin(tar_theta * math.pi / 180)
WeightY = +math.cos(tar_theta * math.pi / 180)
WeightT = 0.01
KP , KD = 100, 100
#print(WeightX, WeightY, WeightT)

#小车运行时间
Time = 10

posDeterminant = []

car = MyCarClass(curPos)
carPre = MyCarClass(prePos)
carTarget = MyCarClass(targetPos)


def calc_Omega():
    '''
        根据PID计算
    '''
    
    data_Delta = np.mat([[1, 0], [-1, -1], [0, 1]])
    data_PD = np.mat([[KP], [KD]])
    data_Weight = np.mat([[WeightX], [WeightY], [WeightT], [0], [0]])
    # print(data_PD)
    data_M = np.mat(np.ones((3, 5)))
    data_M[0] = carTarget.dataArray()
    data_M[1] = car.dataArray()
    data_M[2] = carPre.dataArray()
    data_M = np.transpose(data_M)
    
    # print(data_M)
    data_Re = np.dot(data_M, data_Delta)
    print(data_Re)
    data_Re = np.dot(data_Re, data_PD)
    
    data_Re = np.transpose(data_Re)
    # print(data_Re)
    data_Re = np.dot(data_Re, data_Weight)

    omega = float(data_Re)
    # print(omega)
    
    # limit
    limit = 90
    if omega > limit:
        omega = limit
    if omega < -limit:
        omega = -limit
    
    return float(omega);


#pos_Zoo = np.mat(carTarget.dataArray() + car.dataArray() + carPre.dataArray())
# print(pos_Zoo)
for i in range(0, Time * 100):

    carPre = car
#    car.calc_CarPos_after10ms(v,calc_Omega())
    car.calc_CarPos_after10ms(1,30)
    
    posDeterminant.append(car.dataArray())

print(posDeterminant)

drawCarPos(posDeterminant, 0.01)
