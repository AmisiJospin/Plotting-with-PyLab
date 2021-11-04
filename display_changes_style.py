# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:38:16 2021

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
plt.plot(mySamples, myLinear, 'b-', linewidth=2.0, label='Linear')
plt.plot(mySamples, myQuadratic, 'ro',linewidth=3.0, label='Quadratic')
plt.legend(loc='upper left')

plt.figure('Cube Expose')
plt.clf()
plt.plot(mySamples, myCubic, 'k^', linewidth=4.0, label='Cubic')
plt.plot(mySamples, myExponential, 'r--', linewidth=5.0, label='Exponential')
plt.legend()
plt.figure('Line Quad')
plt.title('Linear vs. Quadratic')
plt.figure('Cube Expose')
plt.title('Cube vs. Exponential')