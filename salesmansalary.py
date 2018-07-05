#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:03:07 2018

@author: bromount
"""

name = str(raw_input("Your Name : "))
emp_id = str(raw_input("Your Employee ID : "))
grade = str(raw_input("Whats your grade (G1/G2) : "))

if grade =='G1':
    basic_salary = 2000
    bonus = 200
    commision=0.02
    sales = int(raw_input("Number of camera sold for the month : "))    
    camera_price = int(raw_input("Whats the MRP of camera : "))
    bonus *=sales
    commision *=camera_price
    grand_salary = basic_salary+bonus+commision
    print "Your Salary for this month is ",grand_salary
    
elif grade =='G2':
    basic_salary = 2500
    bonus = 250
    commision=0.04
    sales = int(raw_input("Number of camera sold for the month : "))    
    camera_price = int(raw_input("Whats the MRP of camera : "))
    bonus *=sales
    commision *=camera_price
    grand_salary = basic_salary+bonus+commision
    print "Your Salary for this month is ",grand_salary
    
else:
    print "You are not in this category check your supervisor"