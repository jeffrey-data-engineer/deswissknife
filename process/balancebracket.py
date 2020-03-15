def shiftright(s):
    l=s.find(')')
    if l>-1:
        r=s.find('(',l)
        if r>-1:
            return ''.join([s[0:l],s[r],s[l+1:r],s[l],s[r+1:]])


def balance_bracket(n):
    # Your code here!
    s="()"*n
    e="("*n+")"*n
    r=[]
    if n<=1:
        r.append(s)
        return r
    else:
        r.append(s)
        while s!=e:
            s=shiftright(s)
            r.append(s)
        return r