# -*- coding: utf-8 -*-
"""Project_Euler_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uPmMRXteZ-RBQprU5mYXKNSSiaCvtFUj
"""

import numpy as np

x = range(1,1000)

y = []

for i in x:
  if i%3 == 0:
    y.append(i)
  elif i%5==0:
    y.append(i)

z = sum(y)

print(z)

6%3

x = [2,3]

x.append(3)

x

