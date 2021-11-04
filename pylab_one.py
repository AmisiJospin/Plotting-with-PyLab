# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:51:22 2021

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
plt.title('Linear')
plt.xlabel('Sample of points')
plt.ylabel('Linear Function')
plt.plot(mySamples, myLinear)

plt.figure('Quadre')
plt.clf()
plt.title('Quadratic')
plt.xlabel('Sample of points')
plt.ylabel('Quadratic Function')
plt.plot(mySamples, myQuadratic)

plt.figure('Cube')
plt.clf()
plt.title('Cubic')
plt.xlabel('Sample of points')
plt.ylabel('Cubic Function')
plt.plot(mySamples, myCubic)

plt.figure('Exposent')
plt.clf()
plt.title('Exponential')
plt.xlabel('Sample of points')
plt.ylabel('Exponential Function')
plt.plot(mySamples, myExponential)
