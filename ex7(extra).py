from matplotlib import pyplot as plt
import numpy as np
file = np.genfromtxt('data.csv',delimiter=",")
x = file[:, 0]
y = file[:, 1]
plt.figure()
plt.plot(x,y, color = 'darkred', linestyle = '--')
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.title('График зависимотси Y от X')
plt.show()
