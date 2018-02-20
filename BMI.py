#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:09:57 2018

@author: bromount
"""

wt = input ("what is your weight in Kg?")

if wt > 200:
    ans= raw_input("Hope the weight is in Kilo Grams !")
    if ans in ('yes','y','s'):
        wt = wt
    else:
        wt = input ("Please provide your weight in Kilo Grams : ")

ht = input ("What is your height cm ?")

ht_metres =  ht / 100.0

print ht_metres

#bmi_deno = ht_metres * ht_metres

#print bmi_deno

def bmi_calculator(weight,height):
    bmi = weight / float(height * height)
    if bmi < 18.5:
        print "Your bmi is ",bmi," and you are under weight"
    elif bmi < 25:
        print "Your bmi is ",bmi," and you are Normal"
    elif bmi < 30:
        print "Your bmi is ",bmi," and you are Over weight"
    else:
        print "Your bmi is ",bmi," and you have obesity"
        

bmi_calculator(wt,ht_metres)