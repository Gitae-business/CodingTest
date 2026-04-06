# 선분 그룹 https://www.acmicpc.net/problem/2162
import sys
from collections import Counter
input = sys.stdin.readline

parent = []

def main():
    global parent

    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    parent = [i for i in range(N)]

    for i in range(N):
        for j in range(i):
            if is_connected(lines[i], lines[j]):
                union(i, j)

    roots = [find(i) for i in range(N)]
    print(len(set(roots)))

    counter = Counter(roots)
    print(max(counter.values()))

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

def ccw(ax, ay, bx, by, cx, cy):
    value = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def is_connected(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    a = ccw(x1, y1, x2, y2, x3, y3)
    b = ccw(x1, y1, x2, y2, x4, y4)
    c = ccw(x3, y3, x4, y4, x1, y1)
    d = ccw(x3, y3, x4, y4, x2, y2)

    ab = a * b
    cd = c * d

    if ab == 0 and cd == 0:
        if (x1, y1) > (x2, y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        if (x3, y3) > (x4, y4):
            x3, y3, x4, y4 = x4, y4, x3, y3
        return not ((x2, y2) < (x3, y3) or (x4, y4) < (x1, y1))

    return ab <= 0 and cd <= 0

if __name__ == '__main__':
    main()
