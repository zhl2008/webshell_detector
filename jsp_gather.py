#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
import hashlib
import tencent
import ali

def md5(string):
    return hashlib.md5(string).hexdigest()
pathdir = '/root/webshell_sample'	
wis = 'jsp|jspx'
filepaths = []	    
for fpathe,dirs,fs in os.walk(pathdir):
    for f in fs:
        ppp = os.path.join(fpathe,f)
        if os.path.isfile(ppp) and re.match(r'^\.('+wis+')$',os.path.splitext(ppp)[1]):
            filepaths.append(ppp)
i = 1
for f in filepaths:
    filename = md5(open(f).read())
    f = f.replace(" ","\\ ")
    f = f.replace("(","\\(")
    f = f.replace(")","\\)")
    f = f.replace("$","\\$")
    f = f.replace("'","\\'")
    print str(i) + " => " + f
    postfix = "." + f.split(".")[-1]
    copy = os.popen("cp " + f + " /root/jsp_sample/" + filename + postfix)
    copy.close()
    i += 1 
