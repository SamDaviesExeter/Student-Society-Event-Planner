from data_strucs import stack_struc

#stack tests 
st = stack_struc.stack()
st.insert_array([1,2,3,4,5,6,7])

def test_reverse():
    assert st.reverse_stack() == [7,6,5,4,3,2,1]

def test_peak():
    assert st.peak() == 7

def test_get_length():
    assert st.get_length() == 7

def test_push_and_pop():
    st.push(8)
    assert st.pop() == 8

def test_empty():
    assert st.is_empty() == False

