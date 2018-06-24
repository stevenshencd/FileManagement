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

global settingFrm

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
    global settingFrm
    settingFrm.mainloop()

def btnDedupeClicked():
    print "dedupe"

def btnBrowseClicked():
    path = tkFileDialog.askdirectory(initialdir=os.getcwd())
    entryPath.delete(0, END)
    entryPath.insert(0, path)


'''
    all configurations are in sysconfig in dictionary type, it is composed of s
    defaultsource:...
    defaultdsnt:...
    syncmap:{source1:dsnt1,source2:dsnt2...}
    lastbackup:date
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
    dict = {'defaultsource': '', 'defaultdsnt': '', 'syncmap': {},'lastbackup':''}
    if not os.path.exists("Config/sysconfig"):
        with open("Config/sysconfig", "w") as f:
            json.dump(dict, f)

def launchSetting():
    settingFrm.mainloop()

# Define APP GUI appearance
root = Tk()
root.title("File Management Tool")
btnSync = Button(root, text = "Sync", relief = GROOVE, command = btnSyncClicked)
btnSync.grid(row = 0, column = 0, sticky = W + E)
btnDedupe = Button(root, text = "Dedupe", relief = GROOVE, command = btnDedupeClicked)
btnDedupe.grid(row = 0, column = 1, sticky = W + E)
btnConfig = Button(root, text = "Config", relief = GROOVE, command = btnConfigClicked)
btnConfig.grid(row = 0, column = 2, sticky = W + E)
lblPath = Label(root, text = "Folder:", relief = FLAT)
lblPath.grid (row = 1, column = 0, sticky = W)
entryPath = Entry(root, relief = GROOVE)
entryPath.grid(row = 1, column = 1, columnspan = 2, sticky = W + E)
btnBrowse = Button(root, text = "Browse", relief = GROOVE, command = btnBrowseClicked)
btnBrowse.grid(row = 1, column = 3, sticky = W + E)
txtResult = Text(root, relief = GROOVE)
txtResult.grid(row = 2, column = 0, columnspan = 4, sticky = W + E + N + S)

root.mainloop()

# Define setting gui


#This procedure is for launch app gui, initialize parameter

def main():
    init()

if __name__ == '__main__':
    print "debug\n"


