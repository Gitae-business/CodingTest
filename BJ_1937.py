# 욕심쟁이 판다 https://www.acmicpc.net/problem/1937
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = 0
ans = -1
board = []
dp = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def main():
    global N, ans, board, dp
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ans = max(ans, dfs(j, i))

    print(ans)

def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not is_in_board(nx, ny):
            continue

        if board[y][x] >= board[ny][nx]:
            continue

        dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)

    return dp[y][x]

def is_in_board(x, y):
    return 0 <= x < N and 0 <= y < N

if __name__ == '__main__':
    main()