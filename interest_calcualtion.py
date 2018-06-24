#!/usr/bin/python

amount = float(input("Enter the Amount : "))
interest_rate= float(input("Enter the interest rate : "))
period= int(input("How many years of investment : "))

value = 0
year = 0
while year <= period:
	value = amount+(interest_rate*amount)
	print "Year %d Rs. %.2f" %(year,value)
	amount = value
	year = year + 1
