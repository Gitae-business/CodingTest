# 구슬 탈출 4 https://www.acmicpc.net/problem/15653
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def tilt_board(r, b, direction, board):
    rx, ry = r['x'], r['y']
    bx, by = b['x'], b['y']
    
    while True:
        cnt = 0
        
        nrx, nry = rx + dx[direction], ry + dy[direction]
        if rx != -1:
            if board[nry][nrx] == 'O':
                rx, ry = -1, -1
                cnt += 1
            elif board[nry][nrx] == '.' and not (nrx == bx and nry == by):
                rx, ry = nrx, nry
                cnt += 1
        
        nbx, nby = bx + dx[direction], by + dy[direction]
        if bx != -1:
            if board[nby][nbx] == 'O':
                bx, by = -1, -1
                cnt += 1
            elif board[nby][nbx] == '.' and not (nbx == rx and nby == ry):
                bx, by = nbx, nby
                cnt += 1
                
        if cnt == 0:
            break
            
    return {'x': rx, 'y': ry}, {'x': bx, 'y': by}

def main():
    N, M = map(int, input().split())
    board = []
    red, blue = {}, {}

    for i in range(N):
        row = list(input().strip())
        for j in range(M):
            if row[j] == 'R':
                red = {'x': j, 'y': i}
                row[j] = '.'
            elif row[j] == 'B':
                blue = {'x': j, 'y': i}
                row[j] = '.'
        board.append(row)

    q = deque([(0, red, blue)])
    visited = set()
    visited.add((red['x'], red['y'], blue['x'], blue['y']))

    while q:
        cost, cur_red, cur_blue = q.popleft()

        for i in range(4):
            nr, nb = tilt_board(cur_red, cur_blue, i, board)
            
            if nb['x'] == -1:
                continue
            
            if nr['x'] == -1:
                print(cost + 1)
                return

            if (nr['x'], nr['y'], nb['x'], nb['y']) not in visited:
                visited.add((nr['x'], nr['y'], nb['x'], nb['y']))
                q.append((cost + 1, nr, nb))

    print(-1)

if __name__ == '__main__':
    main()