# 그림 https://www.acmicpc.net/problem/1926
from collections import deque
import heapq

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    cnt = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False for _ in range(m)] for _ in range(n)]

    def BFS(x, y, visited):
        count = 0
        q = deque()
        q.append((x, y))

        while q:
            sx, sy = q.popleft()
            count += 1
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]

                if (0 <= nx < m) and (0 <= ny < n):
                    if board[ny][nx] == 1 and not visited[ny][nx]:
                        q.append((nx, ny))
                        visited[ny][nx] = True

        heapq.heappush(cnt, -count)

    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                BFS(x, y, visited)

    print(len(cnt))
    print(-heapq.heappop(cnt) if len(cnt) > 0 else 0)
    
if __name__ == '__main__':
    main()
