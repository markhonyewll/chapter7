#!/usr/bin/env python
#-*- utf8 -*-

import os

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)