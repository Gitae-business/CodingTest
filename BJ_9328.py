# 열쇠 https://www.acmicpc.net/problem/9328
from collections import defaultdict, deque

delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def Main():
    t = int(input())

    while t:
        t -= 1
        h, w = map(int, input().split())
        board = [list(input()) for _ in range(h)]

        key = defaultdict(bool)
        for c in input().strip():
            if c != '0':
                key[c] = True

        visited = [[False] * w for _ in range(h)]
        door = defaultdict(list)
        q = deque()

        # 입구 찾기 (가장자리)
        for y in range(h):
            for x in range(w):
                if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                    if board[y][x] != '*':
                        q.append((x, y))
                        visited[y][x] = True

        answer = 0

        while q:
            x, y = q.popleft()

            cell = board[y][x]

            if cell == '$':
                answer += 1
                board[y][x] = '.'
            elif 'A' <= cell <= 'Z':  # 문
                if key[cell.lower()]:
                    board[y][x] = '.'
                else:
                    door[cell].append((x, y))
                    continue
            elif 'a' <= cell <= 'z':  # 열쇠
                if not key[cell]:   # 처음 획득한 경우만
                    key[cell] = True
                    board[y][x] = '.'

                    for (dx, dy) in door[cell.upper()]: # 키가 있으면 문 위치 큐에 삽입
                        q.append((dx, dy))
                    door[cell.upper()] = []

            for (dx, dy) in delta:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < w and 0 <= ny < h:
                    if not visited[ny][nx] and board[ny][nx] != '*':
                        visited[ny][nx] = True
                        q.append((nx, ny))

        print(answer)

if __name__ == '__main__':
    Main()
