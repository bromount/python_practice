#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:32:02 2018

@author: bromount
"""
import pdf_split

#import os

pdf_file_path = raw_input("Enter the path of the PDF file : ")

new_pdf_name = raw_input("Enter the new name you want to save the file : ")

open_file = open(pdf_file_path)

print open_file.read()


#os.open(pdf_file_path,777)
#os.read(pdf_file_path,100)