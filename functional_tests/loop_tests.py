#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:03:40 2018

@author: bromount
"""

for i in range(10):
    print i
    print i,
else:
    print "\nbye bye"
    
while True:
    number = int(raw_input("Enter a positive integer Value : "))
    
    if number < 0:
        continue
    elif number == 0:
        break
    print "Square of the ",number," is", number ** 2
    
print "Bye Bye"
    
for n in range(1,20):
    a = n / 2.0
    print 'half of',n,'is',a
    

for x in range (1,n):
    if x < 10:
        print "Value",x,"is less than 10"
    elif x ==10:
        print "Your value is 10"
    else:
        print "Value",x,"is greater than 10"
        



