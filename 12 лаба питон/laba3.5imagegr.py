# -*- coding: utf-8 -*-
#Напишем простую программу, которая
#загружает картинку из интернета по заданному URL и отображает ее с использованием
#библиотеки Matplotlib:

import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://matplotlib.org/_static/logo2.png')
img = Image.open(BytesIO(response.content))
plt.imshow(img)