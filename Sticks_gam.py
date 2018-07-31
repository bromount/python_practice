#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 12:25:06 2018

@author: bromount
"""

sticks = 21

print "This is a game where you have to pick sticks so does the system :) "

print "There are 21 Sticks available, you have to pick (1-4) at a time. So does the system "

print "Whomever picks the last stick loses the game."

while True:
    print "Sticks Left : ",sticks
    sticks_taken=int(raw_input("Pick Sticks from 1-4 : "))
    if sticks == 1:
        print "you have taken the last stick, you loose"
        break
    if sticks_taken >=5 or sticks_taken <=0:
        print "Wrong choice Select again"
        continue
    print "Computer took : ",(5 - sticks_taken)
    sticks -=5