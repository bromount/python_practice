#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:35:45 2018

@author: bromount
"""

number = int(raw_input("Fibonacci until : "))

a = 0
b = 1

while b <= number:
    print b,
    a,b=b,a+b