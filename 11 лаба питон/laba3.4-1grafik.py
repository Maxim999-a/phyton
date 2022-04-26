# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show()
# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x")    # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y, "r--")    # построение графика