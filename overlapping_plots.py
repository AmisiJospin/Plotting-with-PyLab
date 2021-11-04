# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:04:58 2021

@author: Jospin Amisi
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5*i)

plt.figure('Line Quad')
plt.clf()
plt.plot(mySamples, myLinear, label='Linear')
plt.plot(mySamples, myQuadratic, label='Quadratic')
plt.legend(loc='upper left')

plt.figure('Cube Expose')
plt.clf()
plt.plot(mySamples, myCubic, label='Cubic')
plt.plot(mySamples, myExponential, label='Exponential')
plt.legend()
plt.figure('Line Quad')
plt.title('Linear vs. Quadratic')
plt.figure('Cube Expose')
plt.title('Cube vs. Exponential')