#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Define GUI appearance in this file
main functionality
- folder sync, to add all source file/folders to destination, it can be used as backup purpose
- folder compare, to compare two folders and list files/folders which are not in destination
- batch rename
- folder copy, to move all content from source to destination
GUI appearance
- two folder panel are laid horizontal in the middle of window and occupy most area.
- operation buttons lay in the top of window
- operation information is shown at bottom panel
"""

import os
import re
import time
import shutil
from filemanagement import foldertools
import filemanagement.foldertools

#This procedure is for launch app gui, initialize parameter
def start():
    print "start"
    #defaulpath = os.getcwd()
    if os.name =='nt':
        defaultpath = "c:\\"
    elif os.name == 'posix':
        defaultpath = "/home"
    else:
        defaulpath = os.getcwd()
    print defaultpath
    #destination = os.path.abspath()



if __name__ == '__main__':
    start()