import pyperclip as clp
import time
import sys
from importlib import import_module


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        p, m = sys.argv[1].rsplit('.', 1)
        if len(sys.argv) > 2:
            para = sys.argv[2]
        mod = import_module(p)
        transform = getattr(mod, m)
        tmp_value = clp.paste()
        print("from value: %s" %tmp_value)
        if len(sys.argv) > 2:
            para = sys.argv[2]
            output = transform(tmp_value, para)
        else:
            output = transform(tmp_value)
        if output:
            clp.copy(str(output))
            print("to value: %s" %str(output))
    else:
        print("Usage: clipback.py <module_name>.<function_name>")
