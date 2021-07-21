
def is_palindrome_permuted(str):
    counts = [0] * 256  # ascii range
    for c in str:
        if c != ' ':  # skip whitespace
            counts[ord(c)] += 1

    odd_appeared = False
    for i in counts:
        if i % 2 != 0:
            if odd_appeared:
                return False # odd letter counts can only appear once.
            else:
                odd_appeared = True
    return True


def test_func():
    assert is_palindrome_permuted('tact coa') == True

