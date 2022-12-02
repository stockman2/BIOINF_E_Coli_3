import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log

from pandas import Series

data = open('/home/freeman/Workplace/Prac2/spec1_25mer_histo.txt', 'r')
lines = data.readlines()
spreadshit = {}
for x in lines:
    line = x.split()
    spreadshit[int(line[0])] = int(line[1])
ser: Series = pd.Series(spreadshit)
ser.iloc[1:].plot()
shit_list = []
for key, value in spreadshit.items():
    temp = [key, value]
    shit_list.append(temp)
size_single = sum(x[0]*x[1] for x in shit_list[2:])
size_full = sum(x[0]*x[1] for x in shit_list[4:])
peak = max(shit_list[14:20], key= lambda x: x[1])[0]
proportion = size_single / size_full
print('peak is equal to ' + str(peak))
print('single-region size equal to ' + str(size_single))
print('size_full ' + str(size_full))
print(proportion)
plt.show()
