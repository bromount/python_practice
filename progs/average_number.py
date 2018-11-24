#!/usr/bin/python

N=int(input("How Many Number you want to calcualate : "))
sum = 0
count = 0

while count < N:
	number = float(raw_input("Enter the number : "))
	sum = sum + number
	count = count + 1
	
average = float(sum)/N
print "this is the average of your numbers",average
