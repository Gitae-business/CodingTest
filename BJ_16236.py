from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class Shark:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.level = 2
        self.food = 0

    def eat(self):
        self.food += 1
        if self.food >= self.level:
            self.level += 1
            self.food = 0

    def setLoc(self, x, y):
        self.x = x
        self.y = y

def BFS(board, shark, n):
    q = deque()
    q.append((shark.x, shark.y))

    visited = [[-1] * n for _ in range(n)]
    visited[shark.y][shark.x] = 0

    fish = []
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == -1:
                # 지나갈 수 있는 칸
                if board[ny][nx] <= shark.level:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

                    # 먹을 수 있는 물고기
                    if 0 < board[ny][nx] < shark.level:
                        fish.append((visited[ny][nx], ny, nx))

    if not fish:
        return None  # 먹을 물고기 없음
    
    fish.sort()  # 거리, 위쪽, 왼쪽 우선
    return fish[0]  # (거리, y, x)


def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 아기 상어 위치 찾기
    shark = Shark()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                shark.setLoc(j, i)
                board[i][j] = 0

    ans = 0
    while True:
        target = BFS(board, shark, n)
        if not target:
            break  # 더 이상 먹을 수 없음

        dist, y, x = target
        shark.setLoc(x, y)
        shark.eat()
        board[y][x] = 0
        time += dist

    print(ans)

if __name__ == '__main__':
    main()
