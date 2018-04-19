import parse

import matplotlib.pyplot as plt

acc_data = parse.parse("out.csv")
d = [dat["d"] for dat in acc_data]
t= [dat["time"] for dat in acc_data]

plt.plot(t,d)
#Y_plt.plot(t,y)
#Z_plt.plot(t,z)

plt.show()
