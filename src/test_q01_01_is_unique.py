
def is_unique(string):
    shown = [False] * 256  # ascii range
    for c in string:
        if shown[ord(c)]:
            return False
        else:
            shown[ord(c)] += 1
    return True


def test_func():
    assert is_unique('abc') == True
    assert is_unique('abca') == False
    assert is_unique('dabceb') == False
