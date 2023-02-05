import sys


def slicingTree(parm):
    sliced = 0
    for tree in trees:
        if parm < tree:
            sliced += tree - parm
    return sliced


def paramSearch(start, end, target):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if slicingTree(mid) >= target:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)


def solution():
    global trees
    input = sys.stdin.readline
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    paramSearch(0, 2000000000, m)


solution()