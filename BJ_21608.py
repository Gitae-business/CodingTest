# 상어 초등학교 https://www.acmicpc.net/problem/21608
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    N = int(input())
    prefers = {}
    board = [[0] * N for _ in range(N)]
    answer = 0

    for _ in range(N**2):
        li = list(map(int, input().split()))
        prefers[li[0]] = li[1:]

    def get_near_prefers_and_empty_seats(num, y, x):
        near_prefers = 0
        seats = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny <N):
                continue

            if board[ny][nx] == 0:
                seats += 1
            elif board[ny][nx] in prefers[num]:
                near_prefers += 1

        return near_prefers, seats

    for n in prefers:
        p, s = -1, -1
        ny, nx = -1, -1

        for y in range(N):
            for x in range(N):
                if board[y][x] == 0:
                    tp, ts = get_near_prefers_and_empty_seats(n, y, x)
                    if tp > p:
                        p, s = tp, ts
                        ny, nx = y, x
                    elif tp == p and ts > s:
                        p, s = tp, ts
                        ny, nx = y, x
        
        board[ny][nx] = n

    for y, row in enumerate(board):
        for x, n in enumerate(row):
            p, _ = get_near_prefers_and_empty_seats(n, y, x)
            if p > 0:
                answer += 10 ** (p - 1)

    print(answer)

if __name__ == '__main__':
    main()
