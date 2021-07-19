
def chk_permutation(str1, str2):
    count1 = [0] * 256  # ascii range
    count2 = [0] * 256  # ascii range
    for c in str1:
        count1[ord(c)] += 1
    for c in str2:
        count2[ord(c)] += 1
    return count1 == count2


def test_func():
    assert chk_permutation('abc efg', 'g efabc') == True
    assert chk_permutation('abca', 'cbaa') == True
    assert chk_permutation('abcd', 'cbac') == False
