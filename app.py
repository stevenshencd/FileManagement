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
import json
import tkFileDialog
from Tkinter import *
import filemanagement.foldertools

def btnSyncClicked():
    return
    source = sourcePath.get()
    destination = destinationPath.get()
    if not os.path.isdir(source):
        print "Warning: please select source folder"
        return
    print source + ":" + destination
    filemanagement.foldertools.foldersync(source, destination)

def btnConfigClicked():
    print "Config"

def btnDedupeClicked():
    print "dedupe"

def btnBrowseSourceClicked():
    path = tkFileDialog.askdirectory(initialdir=os.getcwd())
    print path
    sourcePath.delete(0, END)
    sourcePath.insert(0, path)


'''
all config are in sysconfig in dict format, it is composed of 3 parts or more parts
defaultsource:...
defaultdsnt:...
syncmap:{source1:dsnt1,source2:dsnt2...}
'''
def dstnmapping(source):
    fin = open("Config/sysconfig", "r")
    dict = json.load(fin)
    fin.close()
    mapping = dict['syncmap']
    try:
        return mapping[source]
    except:
        return "no found"

def updatedsntmapping(source, dstn):
    d = {}
    with open("Config/sysconfig", "r") as fin:
        d = json.load(fin)
    mapping = d['syncmap']
    mapping[source] = dstn

    with open("Config/sysconfig", "w") as fout:
        json.dump(d,fout)

def init():
    # to check sysconfig file, existed, content
    dict = {'defaultsource': '', 'defaultdsnt': '', 'syncmap': {}}
    if not os.path.exists("Config/sysconfig"):
        with open("Config/sysconfig", "w") as f:
            json.dump(dict, f)

# Define GUI appearance
root = Tk()
root.title("File Management Tool")
btnSync = Button(root, text = "Sync", relief = GROOVE, command = btnSyncClicked)
btnSync.grid(row = 0, column = 0, sticky = W + E)
btnDedupe = Button(root, text = "Dedupe", relief = GROOVE, command = btnDedupeClicked)
btnDedupe.grid(row = 0, column = 1, sticky = W + E)
btnConfig = Button(root, text = "Config", relief = GROOVE, command = btnConfigClicked)
btnConfig.grid(row = 0, column = 2, sticky = W + E)
lblSource = Label(root, text = "Source:", relief = FLAT)
lblSource.grid (row = 1, column = 0, sticky = W)
sourcePath = Entry(root, relief = GROOVE)
sourcePath.grid(row = 1, column = 1, columnspan = 2, sticky = W + E)
btnBrowseSource = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseSourceClicked)
btnBrowseSource.grid(row = 1, column = 3, sticky = W + E)

txtResult = Text(root, relief = GROOVE)
txtResult.grid(row = 2, column = 0, columnspan = 4, sticky = W + E + N + S)

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
    #main()
    #filemanagement.foldertools.foldercompare(source, destination)
    init()
    updatedsntmapping("s1", "d1")
    updatedsntmapping("s2", "d2")
    dstnmapping("s1")
    print dstnmapping("s3")
    updatedsntmapping("s3", "d3")
    '''
    dict ={}
    with open("Config/sys", "r") as fin:
        try:
            dict = json.load(fin)
        except Exception as err:
            print "error happened"

        finally:
            print dict
    print dict '''
