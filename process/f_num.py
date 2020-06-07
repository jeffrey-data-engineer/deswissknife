def sublist(lststr, subtotal):
    if type(lststr)!=list:
        lststr = str(lststr).split(',')
        lst = [int(i) for i in lststr if int(i)<=subtotal]
        lst.sort()
    else:
        lst = [i for i in lststr if i <=subtotal]
    return lst

def bitwiseComplement(raw):
    """
    :type N: int
    :rtype: int
    """
    N = int(raw)
    x = 1
    while x<N:
        x = 2*x+1
    return x-N

def find_subtotal_composition(lststr, subtotal):
    if type(subtotal)!=int:
        subtotal=int(subtotal)
    a = sublist(lststr, subtotal)

    w = []
    for i in range(len(a)):
        sub = subtotal
        c = a.pop()
        sub-=c
        if sub==0:
            w.append([c])
        else:
            if len(a)>0:
                r = find_subtotal_composition(a, sub)
                if r:
                    for i in r:
                        i.append(c)
                        w.append(i)
    return w
