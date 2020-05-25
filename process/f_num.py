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
