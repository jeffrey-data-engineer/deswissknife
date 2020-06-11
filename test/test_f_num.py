from deswissknife.process import f_num

def test_find_subtotal_composition():
    actual = f_num.find_subtotal_composition('1,2,3,4',3)
    assert actual == [[3],[1,2]]

def test_find_subtotal_composition_float():
    actual = f_num.find_subtotal_composition_float('1.2,4,5,2.3,2.24',3.5)
    assert actual == [[1.2,2.3]]