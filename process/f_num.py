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


def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# A Naive recursive Python implementation of LCS problem
def lcs_naive(X, Y, m, n):

    if m == 0 or n == 0:
        return 0;
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_naive(X, Y, m-1, n-1);
    else:
        return max(lcs_naive(X, Y, m, n-1), lcs_naive(X, Y, m-1, n));


# Dynamic programming implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
def lcs_print(X, Y, m, n):
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    # Following code is used to print LCS
    index = L[m][n]

    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1

    return "".join(lcs)