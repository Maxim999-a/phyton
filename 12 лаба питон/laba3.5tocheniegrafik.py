# -*- coding: utf-8 -*-
#Пример построения точечного графика с помощью функции scatter().
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10.5, 0.5)
y = np.cos(x)
plt.scatter(x, y)