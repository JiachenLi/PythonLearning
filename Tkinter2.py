# !/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jiachen Li'

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()

# 成功执行