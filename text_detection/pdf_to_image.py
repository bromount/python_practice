#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:28:42 2018

@author: bromount
"""
from wand.image import Image
# Converting first page into JPG
with Image(filename="document-page1.pdf") as img:
     img.save(filename="/temp.jpg")
# Resizing this image
#with Image(filename="/temp.jpg") as img:
 #    img.resize(200, 150)
  #   img.save(filename="/thumbnail_resize.jpg")
