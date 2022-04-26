# -*- coding: utf-8 -*-

#Пример построения Диаграмма с errorbar элементом.Для этого
#используются параметры xerr, yerr и ecolor (для задания цвета):
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

rnd = np.random.randint
cat_par = [f"P{i}" for i in range(5)]
g1 = [10, 21, 34, 12, 27]

error = np.array([[rnd(2,7),rnd(2,7)] for _ in range(len(cat_par))]).T
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].bar(cat_par, g1, yerr=5, ecolor="r", alpha=0.5, edgecolor="b",
linewidth=2)
axs[1].bar(cat_par, g1, yerr=error, ecolor="r", alpha=0.5, edgecolor="b",
linewidth=2)