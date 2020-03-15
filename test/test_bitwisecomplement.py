from deswissknife.process.bitwisecomplement import Solution

#python -m deswissknife.test.testapp

def test_bitwisecomplement():
    a = 19
    b = Solution()
    c = b.bitwiseComplement(N=a)
    assert c==12