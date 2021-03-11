import math


class MyCarClass(object):
    '''
        单位
    m , m , ° , m/s , °/s
    '''
    x = 0.0
    y = 0.0
    theta = 0.0
    v = 0.0
    omega = 0.0

    def __init__(self, array):
        '''
        Constructor：posture[x,y,theta]
        '''
        if(len(array) == 5):
            self.x = array[0]
            self.y = array[1]
            self.theta = array[2]
            self.v = array[3]
            self.omega = array[4]
        else:
            print('wrong')
    
    def dataArray(self):
        '''
        return：[x,y,theta,v,omega]
        '''
        arr = []
        arr.append(self.x)
        arr.append(self.y)
        arr.append(self.theta)
        arr.append(self.v)
        arr.append(self.omega)
        
        return arr
            
    def calc_CarPos_after10ms(self, v, omega):
        '''
        calculate the car posture after 10ms with v,omega
        '''
        delta_t = 0.01
        self.v = v
        self.omega = omega
        
        delta_L = self.v * delta_t
        delta_Theta = self.omega * delta_t
        
        self.x += delta_L * math.cos((self.theta + delta_Theta / 2) * math.pi / 180)
        self.y += delta_L * math.sin((self.theta + delta_Theta / 2) * math.pi / 180)
        self.theta += delta_Theta
       

if __name__ == '__main__':
    print('程序自身在运行,test')
    arr = [0, 0, 0,1,45]
    car = MyCarClass(arr)
    print(car.dataArray())
    car.calc_CarPos_after10ms(1, 0)
    print(car.dataArray())
else:
    print(' ')
