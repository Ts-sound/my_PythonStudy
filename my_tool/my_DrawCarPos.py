# -- coding: utf-8 --
import matplotlib.pyplot as plt

def drawCarPos(determinant = [[]],timePeriod = 0.01):
    '''
    determinant:    (n,5)  x,y,theta,v,omega
        timePriod: per row data time period (s)
    '''
    t = []
    x,y,theta,v,omega = [],[],[],[],[]
    
    for i in range(0,len(determinant)):
        t.append(i*timePeriod)
          
        x.append(determinant[i][0])
        y.append(determinant[i][1])
        theta.append(determinant[i][2])
        v.append(determinant[i][3])
        omega.append(determinant[i][4])
    
    
    
    # draw by matplotlib
    plt.figure(figsize=(15, 9), dpi=70)

    plt.figure(1)

    # ax1
    ax1 = plt.subplot(231)
    ax1.plot(t, x, 'blue')
    ax1.set(xlabel='t (s)', ylabel='x(m)',
            title="")
    ax1.grid()

    # ax2
    ax2 = plt.subplot(232)
    ax2.plot(t, y)
    ax2.set(xlabel='t(s)', ylabel='y(m)',
            title='')
    ax2.grid()
    
    # ax3
    ax3 = plt.subplot(233)
    ax3.plot(x, y)
    ax3.set(xlabel='x(m)', ylabel='y(m)',
            title='')
    ax3.grid()
    
    # ax4
    ax4 = plt.subplot(234)
    ax4.plot(t, v)
    ax4.set(xlabel='t(s)', ylabel='v(m/s)',
            title='')
    ax4.grid()
    # ax5
    ax5 = plt.subplot(235)
    ax5.plot(t, theta)
    ax5.set(xlabel='t(s)', ylabel='theta(°)',
            title='')
    ax5.grid()
    # ax6
    ax6 = plt.subplot(236)
    ax6.plot(t, omega)
    ax6.set(xlabel='t(s)', ylabel='d(m)',
            title='')
    ax6.grid()
    #
    plt.figure(1)
    
    #
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    print('程序自身在运行,test')
    determinant1 = [[1,2,7,4,5],[1,9,4,4,6]]
    drawCarPos(determinant1, 1)

else:
    print(' ')
