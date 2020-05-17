import pyperclip as clp

def convert_to_row(raw):
    lst = raw.split()
    return ','.join(lst)


if __name__ == '__main__':
    t = clp.paste()
    output = convert_to_row(t)
    print(output)
    clp.copy(output)

