from math import pi, cos, sin
from numpy import abs


class SteerClass(object):
    '''
    classdocs
    '''
    v = 0.0
    x = 0.0
    y = 0.0
    omega = 0.0
    angle = 0.0
    d = 0.0

    def __init__(self, v, angle, x, y):
        '''
        Constructor
        '''
        self.v = v
        self.angle = angle
        self.x = x
        self.y = y
        
    def calcPos(self, omega, delta_t):
      '''
      omega      角速度°/s
      delta_t    经过时间
      
      '''
      
      self.omega = omega 
      
      delta_angle = self.omega * delta_t
      
      self.angle = self.angle + delta_angle
      
      if self.angle > 180 : 
        self.angle -= 360
      elif self.angle < -180:
        self.angle += 180

      angle = self.angle * pi / 180
      
      self.x += -self.v * delta_t * sin(angle)
      self.y += self.v * delta_t * cos(angle)

    def getData(self):
      '''
      determinant:    (n,5)  x,y,angle,v,omega
      '''
      data = []
      
      data.append(self.x)
      data.append(self.y)
      data.append(self.angle)
      data.append(self.v)
      data.append(self.d)
      
      return data


if __name__ == '__main__':
    print('程序自身在运行,test')
    S = SteerClass(1, 0, 0.2, 0)
    S.calcPos(2, 0.1)
    print(S.getData())

else:
    print(' ')
