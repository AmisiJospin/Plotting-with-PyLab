# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:57:34 2021

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
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', linewidth=2.0, label='Linear')

plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'go',linewidth=3.0, label='Quadratic')
plt.legend(loc='upper left')

plt.figure('Cube Expose')
plt.clf()

plt.subplot(121)
plt.ylim(0,14000)
plt.plot(mySamples, myCubic, 'k^', linewidth=4.0, label='Cubic')

plt.subplot(122)
plt.ylim(0,14000)
plt.plot(mySamples, myExponential, 'r--', linewidth=5.0, label='Exponential')
plt.legend()
plt.figure('Line Quad')
plt.title('Linear vs. Quadratic')
plt.figure('Cube Expose')
plt.title('Cube vs. Exponential')