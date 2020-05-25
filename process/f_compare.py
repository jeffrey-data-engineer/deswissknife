def column(a, b):
    s1 = set(a.split())
    s2 = set(b.split())
    ret = []
    ret.append("Left extra: %s" %(s1-s2))
    ret.append("right extra: %s" %(s2-s1))
    return '\n'.join(ret)

def table(a, b, id):
    return a+b+id

