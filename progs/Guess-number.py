#!/usr/bin/python


#Actual Code Starts Here

import random
guesses = 0
number = random.randint(1,1000)
name = raw_input("Hi whats your name?")

print "Hi {0}, Hope you are doing good? Shall we play a game?".format(name)

ans1 = raw_input()

if ans1 in ('s','y','ye','yes'):
    print "I have a number in my mind (1-1000), guess it? \n"
    print "What do you think the number will be?"
    while guesses >=0:
        guess = int(raw_input("Your Guess is : "))
        guesses = guesses + 1
        if guess < number:
            print "WRONG try higher value than", guess
        elif guess > number:
            print "WRONG try lower value than", guess
        else:
            print "You guess it CORRECT; I have the same ",number,"in my mind"
            print "{0}, you have guessed it in {1} attempts".format(name,guesses)
            break
else:
    exit()

