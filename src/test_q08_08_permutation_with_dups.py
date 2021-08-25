
NUM_ASCII = 256

def get_all_permutation(s):
    def permutation(acc_s):
        if len(acc_s) == len(s):
            nonlocal outputs
            outputs += [''.join(acc_s)]
            return

        nonlocal letter_cnt
        for i in range(NUM_ASCII):
            if letter_cnt[i] != 0:
                letter_cnt[i] -= 1
                acc_s += chr(i)
                permutation(acc_s)
                acc_s.pop()
                letter_cnt[i] += 1

    if len(s) == 0:
        return
    letter_cnt = [0] * NUM_ASCII
    for c in s:
        letter_cnt[ord(c)] += 1
    outputs = []
    acc_s = []
    permutation(acc_s)
    return outputs

def is_pass(ret, ans):
    if len(ret) != len(ans): # No duplicate test
        return False
    return False if ans != set(ret) else True


def test_func():
    assert is_pass(get_all_permutation('ab'), {'ab', 'ba'}) == True

    ans = {
        'abc','acb',
        'bac','bca',
        'cab','cba'
    }
    assert is_pass( get_all_permutation('abc'), ans) == True

    ans = {'aba', 'aab', 'baa'}
    assert is_pass( get_all_permutation('aba'), ans) == True

    ans = {
        'aaabb',
        'aabab',
        'abaab',
        'baaab',
        'aabba',
        'ababa',
        'baaba',
        'abbaa',
        'babaa',
        'bbaaa'
    }
    assert is_pass( get_all_permutation('aaabb'), ans) == True
