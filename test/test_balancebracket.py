from deswissknife.process.balancebracket import balance_bracket

def test_balancedbracket():
    for n,exp in [ [0, [""]],
                   [1, ["()"]],
                   [2, ["(())","()()"]]
                   ,[3, ['()()()', '(())()', '(()())', '((()))']]
                   ]:
        actual = balance_bracket(n)
        assert sorted(actual)==sorted(exp)