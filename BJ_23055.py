# 공사장 표지판 https://www.acmicpc.net/problem/23055
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    
    board = [[False] * N for _ in range(N)]
    for i in range(N):
        board[i][0] = True
        board[i][-1] = True
        board[0][i] = True
        board[-1][i] = True

    for i in range(N):
        board[i][i] = True
        board[i][N - i - 1] = True

    
    for i in range(N):
        for j in range(N):
            print('*' if board[i][j] else ' ', end='')
        print()

if __name__ == '__main__':
    main()
