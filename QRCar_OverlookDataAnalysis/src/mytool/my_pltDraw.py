# -- coding: utf-8 --
import matplotlib.pyplot as plt

'''
利用matplotlib画单个图

'''

def drawSinglePicture(x=[], y=[], xlab='x', ylab='y', p_tltle='Figure'):
  
    fig, ax = plt.subplots()
    ax.plot(x, y)
        
    ax.set(xlabel=xlab, ylabel=ylab,
            title=p_tltle)
    ax.grid()
       
    # fig.savefig("test.png")
    plt.show()

# test
# X, Y = [1, 2, 3], [4, 7, 9] 
# drawSinglePicture(X, Y)
