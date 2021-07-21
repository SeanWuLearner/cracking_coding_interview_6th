
# In Python, string is immutable, so it's impossible to perform this in place.
# We can still use list instead to present the idea here.
def urlify(str, str_len):
    str_out = list(str)  # turn string into list
    w_idx = len(str_out) - 1
    for r_idx in range(str_len - 1, -1, -1): # doing it backward
        if str_out[r_idx] == ' ':
            str_out[w_idx] = '0'
            str_out[w_idx-1] = '2'
            str_out[w_idx-2] = '%'
            w_idx -= 3
        else:
            str_out[w_idx] = str_out[r_idx]
            w_idx -= 1
    return ''.join(str_out)

# Most compact solution because String in Python is immutable.
# def urlify(str, str_len):
#     str_out = ''
#     for i in range(str_len):
#         if str[i] == ' ':
#             str_out += "%20"
#         else:
#             str_out += str[i]
#     return str_out


def test_func():
    assert urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'

