#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:01:29 2018

@author: bromount
"""

import math
import random

def math_functions(x):
    return math.sqrt(x)
    

number = math_functions(100)

print number

def math_random(x):
    return random.randint(0,x)


rand = math_random(100)

print rand