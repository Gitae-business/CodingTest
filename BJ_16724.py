# 피리 부는 사나이 https://www.acmicpc.net/problem/16724
dir = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

def main():
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    parent = [i for i in range(n * m)]

    def find(x):
        if parent[x] != x:
            p = find(parent[x])
            parent[x] = p
        return parent[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    result = 0

    for y in range(n):
        for x in range(m):
            idx = y * m + x
            dx, dy = dir[arr[y][x]]
            nx = x + dx
            ny = y + dy
            nidx = ny * m + nx

            if not union(idx, nidx):
                result += 1

    print(result)

if __name__ == '__main__':
    main()
