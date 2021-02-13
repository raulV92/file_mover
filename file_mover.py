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


def file_move(origin:str,destination:str,files:List):
    for f in files:
        #shutil.move(str(Path(os.getcwd(),f)),destination) # printed to test
        shutil.move(str(Path(origin,f)),destination)
        #print(f)

def file_match(file,regex)->str:
    condition=re.compile(regex)
    if condition.search(file):
        return True
    else:
        return False


def confirm():
    return False

def mainFunction(origen:str ,dest:str ,regex:str)->List:
    origin=Path(origen)
    destination=Path(dest)
    moved_files=0
    contents=os.listdir(origin)
    print('contenidos::')
    print(contents)
    to_move=[]
    for file in contents:
        if file_match(file,regex):
            #file_move(destination,file)
            to_move.append(file)
            moved_files +=1
    return to_move


if __name__ == "__main__":
    pass
