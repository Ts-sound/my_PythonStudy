from my_AlgorithmLibrary.ExponentialSmoth import ExpSmoth
import matplotlib.pyplot as plt

x = []
y1 = [0.1514, 0.1514, 0.1429, 0.0434, 0.0423, 0.041, 0.039, 0.038, 0.0371, 0.0356, 0.0345, 0.034, 0.0334, 0.0333, 0.0331, 0.0328, 0.0327, 0.0325, 0.032, 0.0316, 0.0304, 0.0294, 0.0293, 0.0272, 0.027, 0.0266, 0.0263, 0.0253, 0.0256, 0.0247, 0.0241, 0.0234, 0.0231, 0.0215, 0.0218, 0.0208, 0.0203, 0.0201, 0.02, 0.02, 0.02, 0.0195, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y2 = []

Exp = ExpSmoth(0.15, 0.1)

i = 0
for v in y1 :
  i = i + 0.02
  x.append(i)
  y2.append(Exp.Filter(v))

'''
通过plt将数据画出图形
'''
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2, color='red')

ax.set(xlabel="t(s)", ylabel="v(m/s)",
      title="Filter")

ax.grid()

# fig.savefig("test.png")
plt.show()
