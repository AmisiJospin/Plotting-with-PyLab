# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:27:48 2021

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

plt.figure('Line')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)
plt.figure('Line')
plt.title('Linear')
plt.figure('Quad')
plt.title('Quadratic')