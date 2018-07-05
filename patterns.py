#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:51:51 2018

@author: bromount
"""

row = int(raw_input("Enter the row number : "))

n = row
m = row
while n >= 0:
    x = "*"*n
    print x
    n -= 1
    
i = 1

while row >=i:
    x = "*"*i
    print x
    i = i +1
    
while m >= 0:
    x = "*"*m
    y = " "*(row-m)
    print y+x
    m -=1