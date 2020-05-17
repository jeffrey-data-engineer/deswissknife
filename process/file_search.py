#clipboard event
import time
import sys
import os
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip

if __name__ == '__main__':
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            print(recent_value)
        time.sleep(0.1)