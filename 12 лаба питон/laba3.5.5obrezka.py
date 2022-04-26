# -*- coding: utf-8 -*-
#Обрезка графика с помощью функции masked_where
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 5, 0.01)
y = np.cos(x * np.pi)

y_masked = np.ma.masked_where(y < -0.5, y)
plt.ylim(-1, 1)

plt.plot(x, y_masked, linewidth=3)