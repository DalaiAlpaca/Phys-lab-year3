# File: exp4.py
import numpy as np
import os
orange_opened = np.loadtxt(os.path.expanduser("/Users/tiffanygs/Desktop/2020-21/Modules/lab phys/exp 4/20201117/part 4 reflectance/R-orange.txt"),skiprows=17,unpack=True,max_rows=2068)
import matplotlib.pyplot as plt
plt.plot(orange_opened[0],orange_opened[1])
plt.show()