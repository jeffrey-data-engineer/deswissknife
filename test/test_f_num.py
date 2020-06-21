from deswissknife.process import f_num
import time

def test_find_subtotal_composition():
    actual = f_num.find_subtotal_composition('1,2,3,4',3)
    assert actual == [[3],[1,2]]

def test_find_subtotal_composition_float():
    actual = f_num.find_subtotal_composition_float('1.2,4,5,2.3,2.24',3.5)
    actual = [sorted(i) for i in actual]
    assert actual == [[1.2,2.3]]


def test_lcs():
    X = "AGGTAB"
    Y = "GXTXAYB"
    t1 = time.clock()
    actual = f_num.lcs(X, Y)
    print(time.clock() - t1)
    assert actual == 4


def test_lcs_naive():
    X = "AGGTAB"
    Y = "GXTXAYB"
    t1 = time.clock()
    actual = f_num.lcs_naive(X, Y, len(X), len(Y))
    print(time.clock() - t1)
    assert actual == 4


def test_lcs_print():
    X = "AGGTAB"
    Y = "GXTXAYB"
    t1 = time.clock()
    actual = f_num.lcs_print(X, Y, len(X), len(Y))
    print(time.clock() - t1)
    assert actual == 'GTAB'


def test_lcs_print_long():
    a = 'The quick brown fox jumps over a lazy boy.'
    b = 'The slow brown fox jumps over a sick boy.'
    t1 = time.clock()
    actual = f_num.lcs_print(a, b, len(a), len(b))
    print(time.clock() - t1)
    assert actual == 'The  brown fox jumps over a  boy.'