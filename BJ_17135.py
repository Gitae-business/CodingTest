# 캐슬 디펜스 https://www.acmicpc.net/problem/17135
from itertools import combinations

def get_max_killed_enemies(N, M, D, original_board):
    max_killed = 0

    for archer_positions in combinations(range(M), 3):
        board = [row[:] for row in original_board]
        killed_count = 0
        
        for _ in range(N):
            targets = set()
            
            for archer_pos in archer_positions:
                min_dist = float('inf')
                target = None

                for r in range(N - 1, -1, -1):
                    for c in range(M - 1, -1, -1):
                        if board[r][c] == 1:
                            dist = abs(N - r) + abs(archer_pos - c)
                            
                            if dist <= D:
                                if dist < min_dist:
                                    min_dist = dist
                                    target = (r, c)
                                elif dist == min_dist:
                                    if target is None or c < target[1]:
                                        target = (r, c)

                if target is not None:
                    targets.add(target)
            
            for r, c in targets:
                if board[r][c] == 1:
                    board[r][c] = 0
                    killed_count += 1
            
            if _ < N - 1:
                pass
            
            new_board = [[0] * M for _ in range(N)]
            for r in range(N):
                for c in range(M):
                    if board[r][c] == 1 and r + 1 < N:
                        new_board[r+1][c] = 1
            board = new_board

        max_killed = max(max_killed, killed_count)
    return max_killed

def main():
    N, M, D = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = get_max_killed_enemies(N, M, D, board)
    print(result)

if __name__ == '__main__':
    main()