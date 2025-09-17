# 색종이 붙이기 https://www.acmicpc.net/problem/17136
from collections import defaultdict
answer = float('inf')

FILLED = 0
NOT_FILLED = 1
LIMIT = 5

def CheckIsFull(board):
    global answer
    for row in board:
        if NOT_FILLED in row:
            return False
    return True

def CheckIsAttachable(board, x, y, size):
    if x + size > 10 or y + size > 10:
        return False

    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] != NOT_FILLED:
                return False
    return True

def FillBoard(board, x, y, size, value):
    for i in range(y, y+size):
        for j in range(x, x+size):
            board[i][j] = value
    return

def Backtrack(board, counts):
    global answer

    if CheckIsFull(board):
        used = sum(counts[i] for i in range(1, 6))
        answer = min(answer, used)
        return

    for y in range(10):
        for x in range(10):
            if board[y][x] == NOT_FILLED:
                for size in range(5, 0, -1):
                    if counts[size] >= LIMIT:
                        continue
                    
                    if CheckIsAttachable(board, x, y, size):
                        FillBoard(board, x, y, size, FILLED)
                        counts[size] += 1
                        Backtrack(board, counts)

                        counts[size] -= 1
                        FillBoard(board, x, y, size, NOT_FILLED)
                return
    return

def main():
    global answer
    board = [list(map(int, input().split())) for _ in range(10)]
    counts = defaultdict(int)

    Backtrack(board, counts)
    print(answer if answer != float('inf') else -1)

if __name__ == '__main__':
    main()
