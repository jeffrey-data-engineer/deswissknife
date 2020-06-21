from deswissknife.process import f_extract
import time

def test_common():
    a = 'The quick brown fox jumps over a lazy boy.'
    b = 'The slow brown fox jumps over a sick boy.'
    actual = f_extract.common(a,b)
    assert actual == 'The  {0}  brown fox jumps over a  {1}  boy.'


def test_common_longest():
    X = "AGGTAB"
    Y = "GTABb"
    t1 = time.clock()
    actual = f_extract.common_longest(X, Y)
    print(time.clock() - t1)
    print(actual)
    assert actual == 'GTAB'


def test_common():
    X = "AGGTAB"
    Y = "GXTXAYB"
    t1 = time.clock()
    actual = f_extract.common(X, Y)
    print(time.clock() - t1)
    print(actual)
    assert actual == 'A {0} B'