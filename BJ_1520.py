# 내리막 길 https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1
    
    locs = []   # (height, x ,y)
    for y in range(N):
        for x in range(M):
            locs.append((board[y][x], x, y))
    
    locs.sort(reverse=True) # height desc
    
    def is_in_board(nx, ny):
        return 0 <= nx < M and 0 <= ny < N
    
    for _, x, y in locs:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not is_in_board(nx, ny):
                continue

            if board[ny][nx] < board[y][x]:
                dp[ny][nx] += dp[y][x]
    
    print(dp[N-1][M-1])

if __name__ == "__main__":
    main()