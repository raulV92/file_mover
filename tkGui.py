## tkinter gui version

import file_mover as fm
import pretty_errors

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import re
from pathlib import Path
import os
from typing import List


def get_dir(textBox: tk.Entry, type_:str = 'dir'):
    if type_ == 'dir':
        texto = filedialog.askdirectory()
    elif type_ == 'file':
        texto = filedialog.askopenfilename()

    inTxt = textBox.get()
    textBox.delete(0, len(inTxt))
    textBox.insert(0, texto)


def print_checkbox():
    print(var1.get())


def make_message(intro_message, selected_files: List, end_message) -> str:
    full_message = intro_message + '\n'
    for i, f in enumerate(selected_files):

        full_message = full_message + f'{i+1}) ' + f + '\n'
    full_message = full_message + '\n' + end_message
    return full_message


def mainTk_move(from_, to_, reg_ex):
    #breakpoint()
    if len(from_) > 1 and from_[1].get() == 1:  # if checkVar.get()==1:
        origen = '/home/' + os.getlogin() + '/Downloads'
    else:
        origen = from_[0].get()

    dest = to_.get()

    selected_files = fm.filter_files(origen, reg_ex.get())
    intro_message = 'Files selected to move:\n'
    end_message = f'{len(selected_files)} files to {dest}'

    full_message = make_message(intro_message, selected_files, end_message)

    confirm = messagebox.askokcancel("Question", full_message)
    if confirm:
        fm.file_move(origen, dest, selected_files)
        messagebox.showinfo('Process Completed',
                            f'{len(selected_files)} Moved.')
    else:
        pass
        messagebox.showinfo('Process Completed', 'Operation cancelled')


def mainTk_rename(from_, reg_ex, replace, prefix, suffix):

    selected_files = fm.filter_files(from_.get(), reg_ex.get())
    new_names = ['' for _ in range(len(selected_files))]

    for i, f in enumerate(selected_files):
        if not replace[1].get():
            new_names[i] = re.sub(reg_ex.get(), replace[0].get(), f)
        else:
            new_names[i] = f

        if not prefix[1].get():
            new_names[i] = prefix[0].get() + new_names[i]

        if not suffix[1].get():
            separate_ext = os.path.splitext(new_names[i])
            new_names[i] = separate_ext[0] + suffix[0].get() + separate_ext[1]

    if replace[1].get() and prefix[1].get() and suffix[1].get():
        new_names = selected_files
        
    intro_message = f'New names for {len(new_names)} files:\n'
    end_message = f'Selec OK to change the name...'
    full_message = make_message(intro_message, new_names, end_message)
    confirm = messagebox.askokcancel("Question", full_message)
    if confirm:
        fm.rename(zip(selected_files,new_names),Path(from_.get()))
        messagebox.showinfo('Process Completed',
                            f'{len(selected_files)} renamed.')
    else:
        messagebox.showinfo('Process Completed', 'Operation cancelled')
    
    print(list(zip(selected_files, new_names)))
    #breakpoint()

def mainTk_unzip(zipped_textBox, output_dir=None):
    
    zipped_file = zipped_textBox.get()
    fm.unzip_file(zipped_file, output_dir)
    messagebox.showinfo('Process Completed', f'{zipped_file} extracted')

### My widgets:


def path_text_with_button(tab_,
                          ln_label,
                          btn_label,
                          y_axis,
                          default_btn=False,
                          def_label='Default',
                          get_type='dir'):
    # Main Line
    tk.Label(tab_, text=ln_label).place(x=30, y=y_axis)
    folder1 = tk.StringVar()
    sourceBox = tk.Entry(tab_, width=45, textvariable=folder1)
    sourceBox.place(x=80, y=y_axis)
    sourceBtn = tk.Button(tab_,
                          text=btn_label,
                          activebackground="pink",
                          activeforeground="blue",
                          command=lambda: get_dir(sourceBox,get_type))
    sourceBtn.place(x=365, y=y_axis)

    # Optional default button
    if default_btn:
        checkVar = tk.IntVar()
        defaultBox = tk.Checkbutton(tab_, text=def_label, variable=checkVar)
        defaultBox.place(x=80, y=y_axis + 20)
        return (sourceBox, checkVar)

    return (sourceBox)


def label_with_text(tab_, ln_label, y_axis, x_axis=30):
    rExp = tk.Label(tab_, text=ln_label)
    rExp.place(x=x_axis, y=y_axis)
    textBox = tk.Entry(tab_)
    textBox.place(x=x_axis + 50, y=y_axis)

    return textBox


def label_text_check(tab_, ln_label, btn_label, y_axis, x_axis=30):
    text_box = label_with_text(tab_, ln_label, y_axis, x_axis)
    checkVar = tk.IntVar()
    ignoreBox = tk.Checkbutton(tab_, text=btn_label, variable=checkVar)
    ignoreBox.place(x=x_axis + 50, y=y_axis + 20)
    return (text_box, checkVar)


# GUI Set Up:


def draw_mover_tab(tab_name: str):
    tab_move = ttk.Frame(tabControl)
    tabControl.add(tab_move, text=tab_name)
    tabControl.pack(expand=1, fill="both")

    from_dir = path_text_with_button(tab_move,
                                     "From...",
                                     "Browse...",
                                     50,
                                     default_btn=True,
                                     def_label='Downloads')
    to_dir = path_text_with_button(tab_move, "To...", "to...", 100)
    reg_ex = label_with_text(tab_move, "RegExp", 140)

    tk.Button(tab_move,
              text="Move",
              activebackground="pink",
              activeforeground="blue",
              command=lambda: mainTk_move(from_dir, to_dir, reg_ex)).place(
                  x=30, y=180)


def draw_rename_tab(tab_name: str):
    tab_rename = ttk.Frame(tabControl)
    tabControl.add(tab_rename, text=tab_name)
    tabControl.pack(expand=1, fill="both")

    #path_text_with_button(ln_label,btn_label,y_axis,default_btn=False,def_label='Default'):

    from_dir = path_text_with_button(tab_rename, "From...", "Browse...", 50)

    col2 = 220
    reg_ex = label_with_text(tab_rename, "RegExp", 100)
    replace = label_text_check(tab_rename,
                               "Replace",
                               "Ignore",
                               100,
                               x_axis=col2)
    prefix = label_text_check(tab_rename, "Prefix", "Ignore", 140)
    suffix = label_text_check(tab_rename, "Suffix", "Ignore", 140, x_axis=col2)

    tk.Button(tab_rename,
              text="Rename",
              activebackground="pink",
              activeforeground="blue",
              command=lambda: mainTk_rename(from_dir, reg_ex, replace, prefix,
                                            suffix)).place(x=30, y=190)

def draw_unzip_tab(tab_name:str):
    
    tab_unzip = ttk.Frame(tabControl)
    tabControl.add(tab_unzip, text=tab_name)
    tabControl.pack(expand=1, fill="both")

    zipped_file = path_text_with_button(tab_unzip,
        "select file",
        "Browse...",
        50,
        get_type='file')
    # fm.unzip_file(zipped_file)
    tk.Button(tab_unzip,
              text="unZip",
              activebackground="pink",
              activeforeground="blue",
              command=lambda: mainTk_unzip(zipped_file)
              ).place(x=30, y=180)
              




os.chdir(Path.home())
root = tk.Tk()
root.title('File mover and bulk rename')
root.geometry("550x250")
tabControl = ttk.Notebook(root)

draw_mover_tab('File Mover')
draw_rename_tab('Rename')
draw_unzip_tab('unZip')

root.mainloop()
