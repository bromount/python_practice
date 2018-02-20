# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:32:20 2018

@author: bromount
"""

my_name = 'Annamalai Arunachalam'
my_age = 32 # not a lie
my_height = 70 # inches
my_weight = 66 # kgs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d KG heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)