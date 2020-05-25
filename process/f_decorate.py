def between_row(raw,pattern):
    lst = raw.split()
    new_line = "\n%s\n"%pattern
    return new_line.join(lst)



