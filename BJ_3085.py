# 사탕 게임 https://www.acmicpc.net/problem/3085
import sys
input = sys.stdin.readline

N = 0
board = []

def main():
    global N, board
    N = int(input())
    board = [[c for c in input().strip()] for _ in range(N)]
    
    ans = 0
    for i in range(N):
        for j in range(1, N):
            if board[i][j-1] != board[i][j]:
                board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
                ans = max(ans, search())
                board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
    
    for j in range(N):
        for i in range(1, N):
            if board[i-1][j] != board[i][j]:
                board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
                ans = max(ans, search())
                board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
    
    print(ans)

def search():
    mx = 0
    for i in range(N):
        temp = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                temp += 1
                mx = max(mx, temp)
            else:
                temp = 1

    for j in range(N):
        temp = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
                temp += 1
                mx = max(mx, temp)
            else:
                temp = 1

    return mx

if __name__ == '__main__':
    main()
