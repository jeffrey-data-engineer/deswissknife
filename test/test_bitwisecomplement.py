from deswissknife.process.bitwisecomplement import Solution

def test_bitwisecomplement():
    a = 19
    b = Solution()
    c = b.bitwiseComplement(N=a)
    assert c==12