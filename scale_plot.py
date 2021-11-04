# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:12:58 2021

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
    
plt.figure('Cube Expo Log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='Cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r', label='Exponential', linewidth=4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('Cube Expo Linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='Cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r', label='Exponential', linewidth=4.0)
plt.legend()
plt.title('Cubic vs. Exponential')
