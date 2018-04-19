# this module does FFT for  the data within a timed window.
import numpy as np
import parse as ps
import matplotlib.pyplot as plt
import math
acc_dat = ps.parse("out.csv")
x = [math.sin(i/10 * math.pi) for i in range(100)]
t = [i for i in range(100)]

x = [dat["d"] for dat in acc_dat]
t = [dat["time"] for dat in acc_dat]
x2 = np.hamming(len(x)) * x
print(x2-x)
xf = np.fft.fft(x2)
print(xf)
plt.plot(range(len(xf)),xf)
plt.show()

# 配套蓝牙模块
# SVM
