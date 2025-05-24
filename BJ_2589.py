# 보물섬 https://www.acmicpc.net/problem/2589
from collections import deque

def main():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def BFS(sx, sy):
        visited = [[-1] * m for _ in range(n)]
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] = 0
        mx = 0

        while q:
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 'L' and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        mx = max(mx, visited[nx][ny])
                        q.append((nx, ny))
        return mx

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'L':
                answer = max(answer, BFS(i, j))

    print(answer)

if __name__ == '__main__':
    main()
