# -*- coding: utf-8 -*-
#Пример построения точечного графика с помощью функции scatter() с изменение цвета 

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
groups = [f"P{i}" for i in range(7)]
counts = np.random.randint(3, 10, len(groups))
plt.bar(groups, counts)