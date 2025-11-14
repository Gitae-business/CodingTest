# 상어 중학교 https://www.acmicpc.net/problem/21609
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    score = 0

    def find_biggest_block_group():
        visited = [[False] * N for _ in range(N)]
        blocks = []
        rainbows = -1
        best_std = (-1, -1)

        for y in range(N-1, -1, -1):
            for x in range(N-1, -1, -1):
                if board[y][x] in [-1, 0, None] or visited[y][x]:
                    continue
                
                block_type = board[y][x]
                temp_blocks = []
                temp_rainbows = 0
                temp_rainbow_locs = []

                q = deque([(y, x)])
                visited[y][x] = True

                while q:
                    ty, tx = q.popleft()
                    temp_blocks.append((ty, tx))

                    for i in range(4):
                        ny = ty + dy[i]
                        nx = tx + dx[i]
                        if not (0 <= nx < N and 0 <= ny < N):
                            continue

                        if board[ny][nx] in [block_type, 0] and not visited[ny][nx]:
                            if board[ny][nx] == 0:
                                temp_rainbows += 1
                                temp_rainbow_locs.append((ny, nx))
                            visited[ny][nx] = True
                            q.append((ny, nx))
                
                for ry, rx in temp_rainbow_locs:
                    visited[ry][rx] = False

                normal_blocks = [(a, b) for (a, b) in temp_blocks if board[a][b] != 0]
                if not normal_blocks:
                    continue
                std_y, std_x = min(normal_blocks)

                if len(temp_blocks) > len(blocks):
                    blocks = temp_blocks
                    rainbows = temp_rainbows
                    best_std = (std_y, std_x)
                elif len(temp_blocks) == len(blocks):
                    if temp_rainbows > rainbows:
                        blocks = temp_blocks
                        rainbows = temp_rainbows
                        best_std = (std_y, std_x)
                    elif temp_rainbows == rainbows:
                        if (std_y, std_x) > best_std:
                            blocks = temp_blocks
                            rainbows = temp_rainbows
                            best_std = (std_y, std_x)

        return blocks
    
    def del_blocks(blocks):
        nonlocal board
        for block in blocks:
            y, x = block
            board[y][x] = None
        return

    def rotate_ccw():
        nonlocal board
        new_board = []
        for i in range(N-1, -1, -1):
            new_board.append([row[i] for row in board])

        board = new_board
        return
    
    def drop_blocks():
        nonlocal board
        for x in range(N):
            for y in range(N-1, -1, -1):
                block = board[y][x]
                if block == -1 or block is None:
                    continue

                drop_y = y
                for i in range(y+1, N):
                    if board[i][x] == None:
                        drop_y = i
                    else:
                        break
                
                if drop_y != y:
                    board[y][x], board[drop_y][x] = board[drop_y][x], board[y][x]
        return
    
    def print_board():
        print("="*3*N)
        for row in board:
            print(*row)
        print()

    while 1:
        blocks = find_biggest_block_group()
        if len(blocks) < 2:
            break

        score += len(blocks) ** 2
        
        del_blocks(blocks)
        drop_blocks()
        rotate_ccw()
        drop_blocks()
        # print_board()
    print(score)

if __name__ == '__main__':
    main()
