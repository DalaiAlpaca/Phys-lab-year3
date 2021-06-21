# File: exp4.py


import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm


# DATA

orange_opened = np.loadtxt(os.path.expanduser("/Users/tiffanygs/Desktop/Durham 2020-21/Year 3/Lab/lab phys/exp 4/20201117/part 4 reflectance/R-orange.txt"),skiprows=17,unpack=True,max_rows=2068)

orange_refl = orange_opened[1]/100
orange_trans = ((1-orange_refl)**2)/(2*orange_refl) #transform reflection

orange_abs_acetone = np.loadtxt(os.path.expanduser("/Users/tiffanygs/Desktop/Durham 2020-21/Year 3/Lab/lab phys/exp 4/20201117/part 4 reflectance/acetone ora one.txt"),skiprows=17,unpack=True,max_rows=2068)
orange_abs_sample = np.loadtxt(os.path.expanduser("/Users/tiffanygs/Desktop/Durham 2020-21/Year 3/Lab/lab phys/exp 4/20201117/part 4 reflectance/sample orange 1.txt"),skiprows=17,unpack=True,max_rows=2068)

orange_abs_subsolvent = np.log10(orange_abs_acetone[1]/orange_abs_sample[1]) #subtract solvent spectrum
orange_abs = (orange_abs_sample[0],orange_abs_subsolvent)


# FORMATTING

mpl.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1

colors = cm.get_cmap('tab10', 8) #for colour maps, not used here

fig = plt.figure(figsize=(10, 7))
 
ax = fig.add_subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tick_params(axis='both',which='both', reset='True',size=5, width=1, direction='out', bottom='True', top='', left='True', right='')

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(50))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))

ax.set_xlabel('Wavelength / nm')
ax.set_ylabel('Absorbance / AU')

plt.xlim([300,800])
plt.ylim([0,0.7])


# PLOT, SAVE, SHOW

plt.plot(orange_opened[0],orange_trans,linewidth=0.75,c = 'deepskyblue',label='Reflectance') #absorption spectrum from transforming a reflection spectrum

plt.plot(orange_abs[0],orange_abs[1], linewidth=0.75,c = 'tomato',label='Absorbance') #regular absorbance spectrum, with solvent spectrum subtracted 

#plt.savefig('/Users/tiffanygs/Desktop/Name.png') #save as Name.png by removing #

plt.show()