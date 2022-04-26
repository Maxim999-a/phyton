# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(123)
data = np.random.rand(5, 7)
plt.pcolormesh(data, cmap='plasma', edgecolors="k", shading='flat')