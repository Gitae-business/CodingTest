# 연구소 3 https://www.acmicpc.net/problem/17142
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    viruses = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]
    answer = INF

    def bfs(active):
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for x, y in active:
            q.append((x, y))
            dist[x][y] = 0

        max_time = 0
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] != 1 and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    if dist[i][j] == -1:
                        return INF
                    max_time = max(max_time, dist[i][j])
        return max_time

    for active in combinations(viruses, m):
        answer = min(answer, bfs(active))

    print(answer if answer != INF else -1)

if __name__ == '__main__':
    main()