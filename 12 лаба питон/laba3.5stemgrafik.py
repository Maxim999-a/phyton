# -*- coding: utf-8 -*-
#Пример построения Stem-графика 

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10.5, 0.5)
y = np.array([(-0.2)*i**2+2*i for i in x])

plt.stem(x, y)