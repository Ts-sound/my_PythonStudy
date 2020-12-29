import matplotlib.pyplot as plt

def drawSinglePicture(x=[], y=[], xlab='x', ylab='y', p_tltle='Figure'):
  '''
        利用matplotlib画单个图
    (x轴数据，y轴数据，x标签，y标签，标题)

  '''

  fig, ax = plt.subplots()
  ax.plot(x, y)
      
  ax.set(xlabel=xlab, ylabel=ylab,
          title=p_tltle)
  ax.grid()
       
  #fig.savefig("test.png")
  plt.show()



if __name__ == '__main__':
  X, Y = [1, 2, 3], [4, 7, 9] 
  drawSinglePicture(X, Y)
else:
    print ('')

