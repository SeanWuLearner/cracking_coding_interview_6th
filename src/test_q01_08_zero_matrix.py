
def set_row_col_val(arr, r, c, val):
    for i in range(len(arr)):
        arr[i][c] = val
    for i in range(len(arr[0])):
        arr[r][i] = val

def zero_matrix(q):
    if len(dim(q)) != 2:
        raise ValueError

    # set corresponding row-colon to a intermediate value: None
    for i in range(len(q)):
        for j in range(len(q[0])):
            if q[i][j] == 0:
                set_row_col_val(q, i, j, None)

    # set the intermediate value to 0
    q = [[q[i][j] if q[i][j] else 0 for j in range(len(q[0]))] for i in range(len(q))]

    return q

def dim(a):
    if type(a) != list:
        return []
    else:
        return [len(a)] + dim(a[0])

def test_func():
    q = [
        [ 0, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10, 0,12],
        [13,14,15,16],
    ]
    a = [
        [ 0, 0, 0, 0],
        [ 0, 6, 0, 8],
        [ 0, 0, 0, 0],
        [ 0,14, 0,16],
    ]
    assert zero_matrix(q) == a

    q = [
        [1, 2, 3, 4, 0],
        [6, 7, 8, 9, 10],
        [0, 12, 13, 14, 0],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 0, 25]
    ]
    a = [
        [0, 0, 0, 0, 0],
        [0, 7, 8, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 17, 18, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert zero_matrix(q) == a
