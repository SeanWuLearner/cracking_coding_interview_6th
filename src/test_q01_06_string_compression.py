
### initial solution
# def str_compression(s):
#     if len(s) == 0:
#         return s

#     out = s[0]
#     letter, count = s[0], 1
#     for i in range(1, len(s)):
#         if s[i] == letter:
#             count += 1
#         else:
#             letter = s[i]
#             out += str(count) + s[i]
#             count = 1
#     out += str(count)

#     print(out)
#     return out if len(out) < len(s) else s

### solution with avoiding string concatenation
def str_compression(s):
    if len(s) == 0:
        return s

    out = [s[0]]
    letter, count = s[0], 1
    for i in range(1, len(s)):
        if s[i] == letter:
            count += 1
        else:
            letter = s[i]
            out.extend((str(count), s[i]))
            count = 1
    out.append(str(count))

    print(out)
    return ''.join(out) if len(out) < len(s) else s


def test_func():
    assert str_compression('aabcccccaaa') == 'a2b1c5a3'
    assert str_compression('abcd') == 'abcd'

