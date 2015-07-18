#!/usr/bin/python
# -*- coding: cp1252 -*-

from Tkinter import *
import tkMessageBox,tkFileDialog
import re

def OnButtonClick():
    target = str(tkFileDialog.askopenfile(title='Open Manga List Location'))
    directory = re.compile("<open file u'(.*)', mode 'r' at \dx\d+>")
    Address = ''.join(re.findall(directory,target))
    Location.delete(0,END)
    Location.insert(0,Address)

def getLocation():
    filename = Browse()
    name = "Location: " + filename.get()
    labelText.set(name)

def getStr():
    return Location.get()

def ProgramClose():
    Address = getStr()
    app.destroy
    return Address

app = Tk()
app.title("MangaFox GUI")

labelText = StringVar()
labelText.set("MangaFox Recent Update Scanner!")
label1 = Label(app,textvariable=labelText, height=1)
label1.pack()

directory = StringVar(None)
Location = Entry(app,width=40, textvariable=directory)
Location.pack()


menubar = Menu(app)         #predefined menu bar!
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Quit", command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

app.config(menu=menubar)


button1 = Button(app,text="Browse", width=20, command=OnButtonClick)
button1.pack(side='left',padx=15,pady=15)
button2 = Button(app,text="OK",width=10, command=ProgramClose)
button2.pack(side='right',padx=15,pady=15)


app.mainloop()

def Extrastuff():
    relStatus = StringVar()
    relStatus.set(None)
    radio1 = Radiobutton(app, text="Single", value="Single", variable = relStatus, command=beenClicked).pack()
    radio1 = Radiobutton(app, text="Married", value="Married", variable = relStatus, command=beenClicked).pack()



