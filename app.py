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
from Tkinter import *


def btnCleanClicked():
    txtContent.insert(END, "clicked")

def btnDelClicked():
    print "Del click"

def btnBrowseClicked():
    path = tkFileDialog.askdirectory(initialdir=os.getcwd())
    entryPath.delete(0, END)
    entryPath.insert(0, path)

# Define GUI appearance
root = Tk()
root.title("Copy processed raw data to processed folder")


btnClean = Button(root, text = "Clean", relief = GROOVE, command = btnCleanClicked)
btnClean.grid(row = 0, column = 0, sticky = W + E)
btnDel = Button(root, text = "Delete", relief = GROOVE, command = btnDelClicked)
btnDel.grid(row = 0, column = 1, sticky = W + E)
labelPath = Label(root, text = "Folder:", relief = FLAT)
labelPath.grid (row = 1, column = 0, sticky = W)
entryPath = Entry(root, relief = GROOVE)
entryPath.grid(row = 1, column = 1, columnspan = 2, sticky = W + E)
btnBrowse = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseClicked)
btnBrowse.grid(row = 1, column = 3, sticky = W + E)
txtContent = Text(root, relief = GROOVE)
txtContent.grid(row = 2, column = 0, columnspan = 4, sticky = W + E + N + S)

root.mainloop()
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
    source = "/home/steven/dataexample/folder1"
    destination = "/home/steven/dataexample/folder4"
    filemanagement.foldertools.foldercompare(source, destination)
