from my_AlgorithmLibrary.PID import PIDClass
from my_AlgorithmLibrary.ExponentialSmoth import ExpSmoth
from my_tool.steerModel import SteerClass
from my_tool.my_DrawCarPos import drawCarPos
from math import sqrt, pow

PID = PIDClass(100, 0, 16000)
Exp = ExpSmoth(0, 0.2)

T = 15
t = 0.01

Count = int(T / t)

angle = 0.0
v = 0.5
x = 0.02
y = 0.0
omega = 0

# #(r,0)
r = 3
d = 0

Steer = SteerClass(v, angle, x, y)

matrix = []

for i in range(0, Count):
  matrix.append(Steer.getData())
  
  d = sqrt(pow(Steer.x - r, 2) + pow(Steer.y - 0, 2)) - r
  Steer.d = d
  omega = - PID.Out(d)
  omega = Exp.Filter(omega)
  Steer.calcPos(omega, t)
  
drawCarPos(matrix, t)
