from deswissknife.process import f_extract

def test_common():
    a = 'The quick brown fox jumps over a lazy boy.'
    b = 'The slow brown fox jumps over a sick boy.'
    actual = f_extract.common(a,b)
    assert actual == 'The  {0}  brown fox jumps over a  {1}  boy.'