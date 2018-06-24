#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkFileDialog
from Tkinter import *
import Tkinter as tk


class settingDialog(tk, Toplevel):
    def __init__(self, self):
        #super().__init__()
        self.title = "Automatic Backup Configuration"
        self.setupUI()

    def setupUI(self):
        settingFrm = Tk()
        settingFrm.title("Automatic Backup Setting")
        lblSource = Label(settingFrm, text = "Source:", relief = FLAT)
        lblSource.grid (row = 0, column = 0, sticky = W)
        self.sourcePath = Entry(settingFrm, relief = GROOVE)
        self.sourcePath.grid(row = 0, column = 1, columnspan = 4, sticky = W + E)
        btnBrowseSource = Button(settingFrm, text = "Browse", relief = GROOVE, command = self.btnBrowseSourceClicked)
        btnBrowseSource.grid(row = 0, column = 5, sticky = W + E)
        lblDstn = Label(settingFrm, text = "Destination:", relief = FLAT)
        lblDstn.grid (row = 1, column = 0, sticky = W)
        self.dstnPath = Entry(settingFrm, relief = GROOVE)
        self.dstnPath.grid(row = 1, column = 1, columnspan = 4, sticky = W + E)
        btnBrowseDstn = Button(settingFrm, text = "Browse", relief = GROOVE, command = self.btnBrowseDstnClicked)
        btnBrowseDstn.grid(row = 1, column = 5, sticky = W + E)


    def btnBrowseSourceClicked(self):
        path = tkFileDialog.askdirectory(initialdir=os.getcwd())
        self.sourcePath.delete(0, END)
        self.sourcePath.insert(0, path)

    def btnBrowseDstnClicked(self):
        path = tkFileDialog.askdirectory(initialdir=os.getcwd())
        self.dstnPath.delete(0, END)
        self.dstnPath.insert(0, path)

if __name__ == '__main__':
    print "debug\n"
    box = settingDialog ()
    box.mainloop()

