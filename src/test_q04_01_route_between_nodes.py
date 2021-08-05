

def helper(graph, cur, target, memo):
    if cur == target:
        return True

    if cur in memo:
        return False
    memo.add(cur)

    if cur in graph:
        reachable = False
        for next in graph[cur]:
            reachable |= helper(graph, next, target, memo)
        return reachable
    return False

def can_reach(graph, start, end):
    memo = set()
    return helper(graph, start, end, memo)


def test_func():

    graph = {
        0: [1],
        1: [2],
        2: [3,4],
        3: [5],
        4: [10],
        5: [6,8],
        6: [7,9],
        7: [],
        8: [9],
        9: [10, 13],
        10: [8, 9, 11, 12],
        11: [13],
        12: [10],
        13: [11]
    }
    assert can_reach(graph, 0, 13) == True

    graph = {
        0: [1],
        1: [2],
        2: [3,4],
        3: [1],
        4: [3],
        5: [6,8],
        6: [7,9],
        7: [],
        8: [9],
        9: [10, 13],
        10: [8, 9, 11, 12],
        11: [13],
        12: [10],
        13: [11]
    }
    assert can_reach(graph, 0, 13) == False
