#!/usr/bin/python
# -*- coding: cp1252 -*-

from Tkinter import *
import tkMessageBox,tkFileDialog

class MangaGUI(Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.title("MangaFox GUI")

        self.labelText = StringVar()
        self.labelText.set("MangaFox Recent Update Scanner!")
        self.label1 = Label(app,textvariable=labelText, height=1)

        self.directory = StringVar(None)
        self.Location = Entry(app,width=40, textvariable=self.directory)

        self.menubar = Menu(app)         #predefined menu bar!
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label="Quit", command=app.destroy)
        self.menubar.add_cascade(label="File",menu=filemenu)
        self.config(menu=menubar)

        self.button1 = Button(self,text="Browse", width=20, command=OnButtonClick)
        self.button1.pack(side='left',padx=15,pady=15)
        self.button2 = Button(self,text="OK",width=10, command=ProgramClose)
        self.button2.pack(side='right',padx=15,pady=15)

    def OnButtonClick():
        target = str(tkFileDialog.askopenfile(title='Open Manga List Location'))
        directory = re.compile("<open file u'(.*)', mode 'r' at \dx\d+>")
        Address = ''.join(re.findall(directory,target))
        Location.delete(0,END)
        Location.insert(0,Address)

    def getStr():
        return Location.get()

    def ProgramClose():
        Address = getStr()
        app.destroy
        return Address
