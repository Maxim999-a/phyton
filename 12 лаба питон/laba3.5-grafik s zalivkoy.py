# -*- coding: utf-8 -*-
#Разбор работы функции plot()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 5, 0.01)
y = np.cos(x*np.pi)
#Отобразим график с заливкой:
plt.plot(x, y, c = "r")
plt.fill_between(x, y)