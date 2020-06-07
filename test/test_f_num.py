from deswissknife.process import f_num

def test_find_subtotal_composition():
    actual = f_num.find_subtotal_composition('1,2,3,4',3)
    assert actual = [[1,2]]