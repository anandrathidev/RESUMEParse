#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:57:51 2018

@author: anandrathi
"""
#/home/ubuntu/RESUMES_K
#fromdos ./ResumeParser.py
#fromdos ./ResumeParser.py ; ./ResumeParser.py "/home/ubuntu/RESUMES_K/"
import os
import sys
import textract
import pathlib
import shlex

rootdir = sys.argv[1]
def Convert2Text(filepath, opath, filename):
  text="NOT FOUND"
  try:
    #filepath = shlex.quote(filepath)
    #ofile = shlex.quote(ofile)
    text = textract.process(filepath)
    if not os.path.exists(opath):
      os.mkdir(opath)
    ofile = opath + "/" + filename
    with open(ofile, 'wb') as dest:
      dest.write(text)
  except Exception as e:
    print("Parse {} exception {}".format(filepath,e))

inpath = str(pathlib.Path(rootdir).parent)
opath = inpath + "/OUTPUT/"
if not os.path.exists(opath):
  os.mkdir(opath)

for folder, subs, files in os.walk(rootdir):
  for filename in files:
    #print(filename)
    opath2 = opath + pathlib.Path(folder).stem
    #print(opath2)
    #print(filename)
    Convert2Text(filepath=os.path.join(folder, filename), opath=opath2, filename=filename)

