import pyperclip as clp
import time
import sys
from importlib import import_module
import compare

if __name__ == '__main__':
    clp.copy("")
    recent_value = ""
    p = []
    for i in range(3):
        while True:
            tmp_value = clp.paste()
            if tmp_value != recent_value:
                p.append(tmp_value)
                recent_value = tmp_value
                break
            time.sleep(0.1)
        print("Value %s has received."%(i+1))
    if p[1]=="noid":
        output = compare.column(p[0],p[2])
    else:
        output = compare.table(p[0],p[2],p[1])
    clp.copy(output)
