
## tkinter gui version

import file_mover as fm

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import re
from pathlib import Path
import os
from typing import List


def get_dir(textBox:tk.Entry):
    texto = filedialog.askdirectory()
    inTxt=textBox.get()
    textBox.delete(0,len(inTxt))
    textBox.insert(0,texto)


def print_checkbox():
    print(var1.get())

def make_message(intro_message,selected_files:List,end_message)->str:
    full_message=intro_message+'\n'
    for i,f in enumerate(selected_files):

        full_message=full_message+f'{i+1}) '+f+'\n'
    full_message=full_message+'\n'+end_message
    return full_message

def mainTk():
    #breakpoint()
    if checkVar.get()==1:
        origen='/home/'+os.getlogin()+'/Downloads'
    else:
        origen=sourceBox.get()


    dest=destBox.get()

    selected_files=fm.mainFunction(origen,dest,expBox.get())
    intro_message='Files selected to move:\n'
    end_message=f'{len(selected_files)} files to {dest}'

    full_message=make_message(intro_message,selected_files,end_message)

    confirm = messagebox.askokcancel("Question",full_message)
    if confirm:
        fm.file_move(origen,dest,selected_files)
        messagebox.showinfo('Process Completed',f'{len(selected_files)} Moved.')
    else:
        pass
        messagebox.showinfo('Process Completed','Operation cancelled')

### GUI Set Up:
os.chdir(Path.home())
root = tk.Tk()

root.geometry("450x250")

# Linea 1
tk.Label(root, text = "From...").place(x = 30,y = 50)
folder1=tk.StringVar()
sourceBox = tk.Entry(root, width=45, textvariable = folder1)
sourceBox.place(x = 80, y = 50)
sourceBtn = tk.Button(root, text = "Browse...", activebackground = "pink", activeforeground = "blue",
            command=lambda : get_dir(sourceBox) )
sourceBtn.place(x = 365, y = 50)

# Linea 2
checkVar = tk.IntVar()
defaultBox=tk.Checkbutton(root, text="Downloads", variable=checkVar)
defaultBox.place(x=80, y=70)

tk.Label(root, text = "To ...").place(x = 30, y = 100)
destBox = tk.Entry(root,width=45)
destBox.place(x = 80, y = 100)
destBtn=tk.Button(root, text = "to...",activebackground = "pink", activeforeground = "blue",
        command=lambda : get_dir(destBox))
destBtn.place(x = 365, y = 100)

rExp = tk.Label(root, text = "RegEx")
rExp.place(x = 30, y = 140)
expBox = tk.Entry(root)
expBox.place(x = 80, y = 140)

#toBrowse=tk.Button(root,text='Browse...',command=ubicacion)
tk.Button(root, text = "Run",activebackground = "pink", activeforeground = "blue",
        command=mainTk ).place(x = 30, y = 180)


root.mainloop()
