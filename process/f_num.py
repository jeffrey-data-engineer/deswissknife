import itertools
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


def dedup(w):
    w.sort()
    return list(w for w,_ in itertools.groupby(w))

def ret_range(lst):
    max = 0
    min = 0
    for i in lst:
        if i>0:
            max+=i
        else:
            min+=i
    return max, min


def find_subtotal_composition_float(lststr, subtotal):
    if type(subtotal)!=float:
        subtotal=float(subtotal)
    if type(lststr)!=list:
        lststr = str(lststr).split(',')
        a = [float(i) for i in lststr]
        a.sort()
    else:
        a = lststr
    # print(a)
    # print(subtotal)
    w = []

    sub = subtotal-a[0]

    if abs(sub)<0.01:
        w.append([a[0]])
        return w
    else:
        if len(a)>1:
            ma,mi = ret_range(a[1:])

            #with this c included
            if (sub<=ma and sub>=mi):
                r = find_subtotal_composition_float(a[1:], sub)
                if r and len(r)>0:
                    #print("with:%s--%s--%s" %(a[1:],sub,r))
                    for j in r:
                        if len(j)>0:
                            j.append(a[0])
                            w.append(j)

            #without this c included
            if (subtotal<=ma and subtotal>=mi):
                t = find_subtotal_composition_float(a[1:], subtotal)
                if t and len(t)>0:
                    #print("without:%s--%s---%s" %(a[1:],subtotal,t))
                    for k in t:
                        if len(k)>0:
                            w.append(k)

    return dedup(w)


def find_subtotal(lststr, subtotal):
    if type(subtotal)!=float:
        subtotal=float(subtotal)
    if type(lststr)!=list:
        lststr = str(lststr).split(',')
        a = [float(i) for i in lststr]
    else:
        a = lststr
    w = []
    for j in range(1,7):
        t = dedup(list(itertools.combinations(a,j)))
        #print(t)
        for i in t:
            if abs(sum(i)-subtotal)<0.01:
                w.append(list(i))
    return w