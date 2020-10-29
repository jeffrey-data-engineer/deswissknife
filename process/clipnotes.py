import pyperclip as clp
import time
import sys
from importlib import import_module

from pynput import keyboard
import time

break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        print ('end pressed')
        break_program = True
        return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        note_name = sys.argv[1]
        clp.copy("")
        recent_value = ""
        with keyboard.Listener(on_press=on_press) as listener:
            with open(note_name,'a') as f:
                while not break_program:
                    tmp_value = clp.paste()
                    if tmp_value != recent_value:
                        f.write(tmp_value.replace('\n',' ') +'\n\n')
                        f.flush()
                        print("note value: %s" %tmp_value)
                        recent_value = tmp_value
                        #break
                    time.sleep(0.1)
    else:
        print("Usage: clipnotes.py <note_name>")
