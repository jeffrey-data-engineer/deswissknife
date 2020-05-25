def distinct(raw):
    lst = raw.split()
    return '\n'.join(set(lst))

def add(raw):
    lst = raw.split()
    total = 0
    for i in lst:
        total += int(i)
    return total

