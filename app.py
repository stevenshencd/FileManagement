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
import tkFileDialog

def btnSyncClicked():
    source = sourcePath.get()
    destination = destinationPath.get()
    if not os.path.isdir(source):
        print "Warning: please select source folder"
        return
    print source + ":" + destination
    filemanagement.foldertools.foldersync(source, destination)

def btnCompareClicked():
    print "Del click"

def btnDedupeClicked():
    print "dedupe"

def btnBrowseSourceClicked():
    path = tkFileDialog.askdirectory(initialdir=os.getcwd())
    print path
    sourcePath.delete(0, END)
    sourcePath.insert(0, path)

def btnBrowseDestinationClicked():
    path = tkFileDialog.askdirectory(initialdir=os.getcwd())
    print path
    destinationPath.delete(0, END)
    destinationPath.insert(0, path)

# Define GUI appearance
root = Tk()
root.title("File Management Tool")
btnSync = Button(root, text = "Sync", relief = GROOVE, command = btnSyncClicked)
btnSync.grid(row = 0, column = 0, sticky = W + E)
btnCompare = Button(root, text = "Compare", relief = GROOVE, command = btnCompareClicked)
btnCompare.grid(row = 0, column = 1, sticky = W + E)
btnDedupe = Button(root, text = "Dedupe", relief = GROOVE, command = btnDedupeClicked)
btnDedupe.grid(row = 0, column = 2, sticky = W + E)
#btnClean = Button(root, text = "Clean", relief = GROOVE, command = btnCleanClicked)
#btnClean.grid(row = 0, column = 0, sticky = W + E)
lblSource = Label(root, text = "Source:", relief = FLAT)
lblSource.grid (row = 1, column = 0, sticky = W)
sourcePath = Entry(root, relief = GROOVE)
sourcePath.grid(row = 1, column = 1, columnspan = 2, sticky = W + E)
btnBrowseSource = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseSourceClicked)
btnBrowseSource.grid(row = 1, column = 3, sticky = W + E)

lblDestination = Label(root, text = "Destination:", relief = FLAT)
lblDestination.grid (row = 1, column = 4, sticky = W)
destinationPath = Entry(root, relief = GROOVE)
destinationPath.grid(row = 1, column = 5, columnspan = 2, sticky = W + E)
btnBrowseDestination = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseDestinationClicked)
btnBrowseDestination.grid(row = 1, column = 7, sticky = W + E)

txtContentSource = Text(root, relief = GROOVE)
txtContentSource.grid(row = 2, column = 0, columnspan = 4, sticky = W + E + N + S)
txtContentDestination = Text(root, relief = GROOVE)
txtContentDestination.grid(row = 2, column = 4, columnspan = 4, sticky = W + E + N + S)
root.mainloop()
#This procedure is for launch app gui, initialize parameter
def main():
    print "main"
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
    main()
    #filemanagement.foldertools.foldercompare(source, destination)

