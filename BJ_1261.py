# 알고스팟 https://www.acmicpc.net/problem/1261
import heapq

INF = int(1e9)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
    n, m = map(int, input().split())  # n: 가로(x), m: 세로(y)
    arr = [list(map(int, input().strip())) for _ in range(m)]

    cost = [[INF] * n for _ in range(m)]
    cost[0][0] = 0
    q = [(0, 0, 0)]  # (부순 벽 수, y, x)

    while q:
        c, y, x = heapq.heappop(q)

        if cost[y][x] < c:
            continue

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = c + arr[ny][nx]
                if cost[ny][nx] > new_cost:
                    cost[ny][nx] = new_cost
                    heapq.heappush(q, (new_cost, ny, nx))

    print(cost[m-1][n-1])

if __name__ == '__main__':
    main()
