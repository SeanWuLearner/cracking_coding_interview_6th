
def one_way(str1, str2):
    # len_diff = abs(len(str1) - len(str2))
    # if len_diff >= 2:
    #     return False

    edited = False
    i1, i2 = 0, 0
    len1, len2 = len(str1), len(str2)
    while i1 < len1 and i2 < len2:
        if str1[i1] == str2[i2]:
            i2 += 1
            i1 += 1
        else:
            if edited is True:
                return False

            edited = True
            if len1 == len2:
                i2 += 1
                i1 += 1
            elif len1 < len2:
                i2 += 1
            else:
                i1 += 1
    return (i1 == len1 and i2 == len2) or (edited is False and ((len1 - i1) + (len2 - i2) <= 1))


def test_func():
    assert one_way('pale', 'ple') == True
    assert one_way('pales', 'pale') == True
    assert one_way('pale', 'bale') == True
    assert one_way('pale', 'bake') == False

