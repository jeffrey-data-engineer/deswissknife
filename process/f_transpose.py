def to_row(raw):
    lst = raw.split()
    return ','.join(lst)

def to_column(raw):
    lst = raw.split(',')
    return '\n'.join(lst)
