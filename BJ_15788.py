# 밸런스 스톤 https://www.acmicpc.net/problem/15788
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    board = []
    zy, zx = -1, -1

    for y in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for x in range(N):
            if row[x] == 0:
                zy, zx = y, x

    target = -1
    for y in range(N):
        if y != zy:
            target = sum(board[y])
            break

    value = target - sum(board[zy])

    if value <= 0:
        print(-1)
        return

    board[zy][zx] = value

    for y in range(N):
        if sum(board[y]) != target:
            print(-1)
            return

    for x in range(N):
        if sum(board[y][x] for y in range(N)) != target:
            print(-1)
            return

    if sum(board[i][i] for i in range(N)) != target:
        print(-1)
        return

    if sum(board[i][N - 1 - i] for i in range(N)) != target:
        print(-1)
        return

    print(value)

if __name__ == '__main__':
    main()