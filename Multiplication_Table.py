#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 15:07:27 2018

@author: bromount
"""

i = 1

print "-"*50

while i <11:
    n = 1
    while n <= 10:
        m = i * n
        print "%4d"%m,
        n += 1
    print " "
    i +=1
print "-"*50