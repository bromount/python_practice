#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 16:25:19 2018

@author: BroMount
"""

n = int(raw_input("How Many Numbers you wanna input : "))
sum = 0
count = 1

while count <=n:
    new_value = float(raw_input("Enter the number : "))
    
    sum = sum + new_value
    count = count+1
    
average = sum / n
print "Average of the above ",n," input is : ",average