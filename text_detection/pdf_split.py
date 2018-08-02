#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:35:19 2018

@author: bromount
"""

from PyPDF2 import PdfFileWriter, PdfFileReader

#Getting Input from user

doc_path=raw_input("Enter the file path with file name : ")

inputpdf = PdfFileReader(open(doc_path, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)  