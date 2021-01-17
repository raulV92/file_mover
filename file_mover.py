"""
Organize files:
input info:
->folder to clean
->regular expression to match
->folder(s) to move

"""
orig=r'C:\Users\vara9003\Pictures\Centro de devoluciones_files'
dest1=r'C:\Users\vara9003\Pictures\Centro de devoluciones_files\organizados\imagenes'
dest2=r'C:\\Users\vara9003\Pictures\Centro de devoluciones_files\organizados\script'

destinies={r'\.jpg$':dest1,
            r'\.png$':dest1,

            r'\.js':dest2,
            r'\.css$':dest2}

import shutil
import os
import re
from pathlib import Path

def file_move(destination,file):
    pass
    shutil.move(str(Path(os.getcwd(),file)),destination)

def file_match(destinies,file)->str:
    
    for exp in destinies.keys():
        patron=re.compile(exp)
        if patron.search(file):
            return destinies[exp]

def folder_scan(f_path): 
    os.chdir(f_path)
    return os.listdir()

if __name__ == "__main__":
    scn_dir=Path(orig)
    contents=folder_scan(Path(orig))
    #print(os.getcwd())
    #print(contents)
    moved_files=0
    for file in contents:
        destination=file_match(destinies,file)
        if destination:
            file_move(destination,file)
            moved_files +=1
    print('Number of moved Files: ',moved_files)
        