#!/usr/bin/env python3
'''
Пример работы с редактируемым текстом
'''

# MORE JUNKER COMMENT

from tkinter import *
import random as r
clr = ("green","blue","red","black","snow")
ind = 0

def colors(k,av=None):
	Txt = Label(root,text="Metka")
	Txt.configure(bg = r.choice(clr),fg = r.choice(clr)) 
	Txt.grid(row = k+1,column=1, sticky="e"+"w"+"s"+"n")

def to_add(*a):
	global ind
	root.columnconfigure(ind+2,weight=1)
	root.rowconfigure(ind+1,weight=2)
	But = Button(root,text="knopka",command = colors(ind))
	But.bind('<Button-1>', lambda av,ind=ind: colors(ind,av))
	But.grid(row=ind+1, column=0, sticky="e"+"w"+"s"+"n")
	ind += 1
	
Root = Tk()
Root.title("Proj1")

root = Frame(Root)
root.place(relheight = 1, relwidth = 1)
root.columnconfigure(1,weight = 1)
root.rowconfigure(1,weight = 1)
But = Button(root, text="Add")
But.bind('<Button-1>', to_add)
But.grid(row=0, column=0, sticky="e"+"w")
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky="e"+"w")

Root.mainloop()
