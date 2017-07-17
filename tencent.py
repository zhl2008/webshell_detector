#!/usr/bin/env python
import re
from config import *
def is_webshell(filepath,filetype):
    if filetype=='php':
	tencent_webshell_rule = tencent_webshell_rule_php
    elif filetype=='jsp':
	tencent_webshell_rule = tencent_webshell_rule_jsp
    content = open(filepath).read()
    for rule in tencent_webshell_rule:
	shell_type = rule[0]
	shell_regrex = rule[3]
	if re.findall(shell_regrex,content):
	    print "[!]webshell find => " + filepath + " shell_type => " + shell_type 
	    return (shell_type,1)
    print "[*]File OK => " + filepath
    return ("OK",0)
     
