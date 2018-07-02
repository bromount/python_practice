#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 14:05:18 2018

@author: BroMount
"""

deposit_money = int(raw_input("Enter Amount : "))
interest_rate = float(raw_input("Interest Rate on your Bank : "))
duration = int(raw_input("How Many YEARS you are depositing : "))

value = 0
years = 1

while years <=duration:
    value = deposit_money + (deposit_money*interest_rate)
    print "For the year",years,"Your savings willbe",value
    years = years +1
    deposit_money=value