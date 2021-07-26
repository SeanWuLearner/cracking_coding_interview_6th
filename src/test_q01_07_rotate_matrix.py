
def rotate_matrix(q):
    n = len(q)
    n_2ceil = int( (n+1) / 2)
    n_2floor = int( n / 2)


    for i in range(n_2ceil):
        for j in range(0, n_2floor):
            q[i][j], q[n-1-j][i], q[n-1-i][n-1-j], q[j][n-1-i] = q[n-1-j][i], q[n-1-i][n-1-j], q[j][n-1-i], q[i][j]

    return q






def test_func():
    q = [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16],
    ]
    a = [
        [13, 9, 5, 1],
        [14,10, 6, 2],
        [15,11, 7, 3],
        [16,12, 8, 4]

    ]
    assert rotate_matrix(q) == a

    q = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    a = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]
    assert rotate_matrix(q) == a
