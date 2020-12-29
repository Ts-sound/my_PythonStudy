

class ExpSmoth(object):
    '''
        指数平滑滤波模型
    '''
    value = 0.0
    a = 0.0  # 权重系数

    def __init__(self, value, a):
      '''
        Constructor
        a为权重系数，取值范围为（0-1.0）
      '''
      self.value = value
      
      if(a > 0 and a < 1):
        self.a = a
       
    def Filter(self, rawValue):
      '''
            传递原始值，返回滤波后的值
      '''
      self.value = self.a * rawValue + (1 - self.a) * self.value
      
      return self.value
