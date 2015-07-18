#!/usr/bin/python
# -*- coding: cp1252 -*-

from Tkinter import *
import tkMessageBox,tkFileDialog

class MangaGUI(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.title("MangaFox GUI")

        self.directory = StringVar(None)
        self.Location = Entry(self,width=40, textvariable=self.directory)
        self.Location.grid(column=0,row=1,columnspan=1,sticky='EW')

        self.labelVariable = StringVar()
        label = Label(self,textvariable=self.labelVariable)
        label.grid(column=0,row=2,columnspan = 1)
        self.labelVariable.set("Please type the location of your MangaList file or Browse to find!")

        self.menubar = Menu(self)         #predefined menu bar!
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Quit", command=self.destroy)
        self.filemenu.add_command(label="Browse", command=self.OnButtonClick)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.config(menu=self.menubar)

        button1 = Button(self,text="Browse", width=20, command=self.OnButtonClick)
        button1.grid(column=2,row=1)
        button2 = Button(self,text="OK",width=10, command=self.ProgramClose)
        button2.grid(column=3,row=1)

    def OnButtonClick(self):
        target = str(tkFileDialog.askopenfile(title='Open Manga List Location'))
        target = target.strip("^<open file u'")
        Local = target[:-26]
        self.Location.delete(0,END)
        self.Location.insert(0,Local)

    def getStr(self):
        return self.Location.get()

    def ProgramClose(self):
        self.Address = self.getStr()
        self.destroy()



if __name__ == '__main__': main()

