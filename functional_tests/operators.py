#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:19:55 2018

@author: bromount
"""

a = 1==0

print a

1>3

N=100
a =2

while a < N:
    print a
    a +=a
    
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(raw_input("Enter the number of inputs sold: "))
price = float(raw_input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print "Bonus        = %0.2f" % bonus
print "Commision    = %7.2f" % commision
print "Gross salary = %6.2f" % (basic_salary + bonus + commision)