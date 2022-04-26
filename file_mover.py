"""
Organize files:
input info:
->folder to clean
->regular expression to match
->folder(s) to move

"""

import shutil
import os
import re
from pathlib import Path
from typing import List

def get_new_name(filtrados, reg_exp,punto_corte):
    ext = re.compile(r'\..{2,5}$')
    new_names = []
    for i in filtrados:
        ext_str = ext.search(i).group()
        inicio = reg_exp.search(i).span()
        # breakpoint()
        new_names.append(i[:inicio[punto_corte]] + str(ext_str))

    return zip(filtrados, new_names)
    
def rename(new_names,folder):
    for old,new in new_names:
        os.rename(Path(folder,old),Path(folder,new))


def file_move(origin:str,destination:str,files:List):
    for f in files:
        #shutil.move(str(Path(os.getcwd(),f)),destination) # printed to test
        shutil.move(str(Path(origin,f)),destination)
        #print(f)

def file_match(file_,regex)->str:
    condition=re.compile(regex)
    if condition.search(file_):
        return True
    else:
        return False


def confirm():
    return False

def filter_files(origen:str,regex:str)->List:
    origin=Path(origen)
    #destination=Path(dest)
    moved_files=0
    contents=os.listdir(origin)
    print('contenidos::')
    print(contents)
    to_move=[]
    for file_ in contents:
        if file_match(file_,regex):
            #file_move(destination,file)
            to_move.append(file_)
            moved_files +=1
    return to_move


if __name__ == "__main__":
    pass
