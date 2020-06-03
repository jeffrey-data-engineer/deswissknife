import pyperclip as clp
import time
import sys
from importlib import import_module
import f_extract

# compare two and get the common in template, differ in parameter
if __name__ == '__main__':
    clp.copy("")
    recent_value = ""
    p = []
    for i in range(2):
        while True:
            tmp_value = clp.paste()
            if tmp_value != recent_value:
                p.append(tmp_value)
                recent_value = tmp_value
                break
            time.sleep(0.1)
        print("Value '%s' has received."%(tmp_value[:20]+'......'))
    output = f_extract.parameter(p[0],p[1])
    clp.copy(output)
    print(output)
