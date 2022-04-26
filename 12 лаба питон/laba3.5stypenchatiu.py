# -*- coding: utf-8 -*-
#Пример построения ступенчатого графика 
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7)
y = x

where_set = ['pre', 'post', 'mid']
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
for i, ax in enumerate(axs):
    ax.step(x, y, "g-o", where=where_set[i])
    ax.grid()