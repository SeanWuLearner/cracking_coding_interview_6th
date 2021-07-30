
def is_substring(s, pat):
    return True if s.find(pat) != -1 else False

def is_string_rotation(a, b):
    a = a + a
    return is_substring(a, b)


def test_func():
    assert is_string_rotation("waterbottle", "erbottlewat") == True
    assert is_string_rotation("waterbottle", "erbottlewata") == False
