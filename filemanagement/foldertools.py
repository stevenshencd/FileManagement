#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
libraries for file comparation, file copy, moving
"""

import os
import re
import time
import shutil

# To compare two files based on attributes, name, modification date
def filecompare(path1, path2):
    print "filecompare"
    if os.path.samefile(path1, path2):
        print "same"
    else:
        print "different"

def backup(source, destination):
    print "backup"

def sync(source, destination):
    print "sync"

def dedupe(source):
    print "dedupe"

def foldersync(source, destination):
    print "folder syn"
    if not os.path.isdir(source):
        print "error: source path is not a valid path"
        return -1
    if not os.path.exists(destination):
        print "warning : destination in not a valid path"
        os.mkdir(destination,0o777)
    for obj in os.listdir(source):
        if os.path.isfile(source + os.sep + obj):
            if findfile(obj,destination) != 0:
                print"to copy ..."
                shutil.copy(source + os.sep + obj,destination)
        else:
            foldersync(source + os.sep + obj, destination + os.sep + obj)

def findfile(filename,folder):
    for obj in os.listdir(folder):
        if filename == obj:
            return 0
    return 1

if __name__ == '__main__':

    source = "/home/steven/dataexample/folder1"
    destination = "/home/steven/dataexample/folder25"
    foldersync(source,destination)

