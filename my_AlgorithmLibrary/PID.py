

class PIDClass(object):
    '''
          常规PID模型
    '''
    Kp = 0
    Ki = 0
    Kd = 0
    
    E = 0  # 当前偏差量
    Ec = 0  # 偏差变化量
    SE = 0  # 历史偏差和

    def __init__(self, kp, ki, kd):
        '''
        Constructor
        '''
        self.Kp = kp
        self.Ki = ki
        self.Kd = kd
        
    def Out(self, E):
        '''
                计算PID输出
        E:偏差量   （目标值 - 当前值）
        '''
        self.Ec = E - self.E;
        self.E = E
        self.SE += E
        
        out = self.Kp * self.E + self.Ki * self.SE + self.Kd * self.Ec
        
        return out
    
    def clear(self):     
      '''
               清除PID数据    
      '''
      self.E = 0
      self.Ec = 0
      self.SE = 0


if __name__ == '__main__':
  l = 10 
  arr = [l]
  PID = PIDClass(0.2, 0, 0.1)
  
  for i in range(0, 20):
    out = PID.Out(0 - l)  # 目标值为0
    l += out
    arr.append(l)
  print(arr)
else:
    print ('')
