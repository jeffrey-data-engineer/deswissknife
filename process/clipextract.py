import pyperclip as clp
import time
import sys
from importlib import import_module

# compare two and get the common in template, differ in parameter
if __name__ == '__main__':
    clp.copy("")
    recent_value = ""
    para = []
    if len(sys.argv) == 2:
        p, m = sys.argv[1].rsplit('.', 1)
        mod = import_module(p)
        transform = getattr(mod, m)

    for i in range(2):
        while True:
            tmp_value = clp.paste()
            if tmp_value != recent_value:
                para.append(tmp_value)
                recent_value = tmp_value
                break
            time.sleep(0.1)
        print("Value '%s' has received."%(tmp_value[:10]+'......'))
    output = transform(para[0],para[1])
    clp.copy(output)
    print(output)
