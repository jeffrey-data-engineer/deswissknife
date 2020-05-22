import pyperclip as clp

def convert_to_row(raw):
    lst = raw.split()
    return ','.join(lst)


if __name__ == '__main__':
    clp.copy("")
    recent_value = ""
    while True:
        tmp_value = clp.paste()
        if tmp_value != recent_value:
            output = convert_to_row(tmp_value)
            recent_value = output
            clp.copy(output)
        time.sleep(0.1)
