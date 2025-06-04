# 종이의 개수 https://www.acmicpc.net/problem/1780
from collections import defaultdict
NOTSAME = 3

def main():
    n = int(input())
    board = [input().split() for _ in range(n)]
    answer = defaultdict(int)

    def isSame(x, y, size):
        past = board[y][x]
        for i in range(y, y+size):
            for j in range(x, x+size):
                if board[i][j] != past:
                    return NOTSAME
        return past

    def divide(x, y, size):
        num = isSame(x, y, size)
        if num != NOTSAME:
            answer[num] += 1
            return
        
        for i in range(y, y+size, size//3):
            for j in range(x, x+size, size//3):
                divide(j, i, size//3)

    divide(0, 0, n)

    idxs = ['-1', '0', '1']
    [print(answer[i]) for i in idxs]

if __name__ == '__main__':
    main()
