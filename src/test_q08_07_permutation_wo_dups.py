
def insert_char_to_list(c, l, idx):
    ret = []
    ret.extend(l[:idx])
    ret += c
    ret.extend(l[idx:])
    return ret

def get_all_permutation(s):
    def permutation(s_idx):
        if s_idx == len(s):
            return
        nonlocal outputs
        new_out = []
        for elem in outputs:
            for i in range(len(elem) + 1):
                new_out += [insert_char_to_list(s[s_idx], elem, i)]
        outputs = new_out
        permutation(s_idx + 1)

    if len(s) == 0:
        return
    outputs = [[s[0]]] # at least one elem in it in order to kickstart permutation()
    permutation(1)
    ret = set()
    for output in outputs:
        ret.add(''.join(output))
    return ret


def test_func():
    assert {'ab', 'ba'} == get_all_permutation('ab')

    ans = {
        'abc','acb',
        'bac','bca',
        'cab','cba'
    }
    assert ans == get_all_permutation('abc')
