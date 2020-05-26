def to_row(raw):
    lst = raw.split()
    return ','.join(lst)

def to_column(raw):
    lst = raw.split(',')
    return '\r\n'.join(lst)

def transpose(raw):
    if('\r\n' in raw):
        return to_row(raw)
    else:
        return to_column(raw)