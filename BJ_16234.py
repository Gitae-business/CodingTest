# 인구 이동 https://www.acmicpc.net/problem/16234
import math
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    while True:
        stop_flag = True
        visited = [[False] * n for _ in range(n)]
        
        for y in range(n):
            for x in range(n):
                if not visited[y][x]:
                    union_blocks = deque([(y, x)])  # 연합이 되는 블록들의 집합
                    block_sum = board[y][x] # 연합의 총 인구
                    
                    q = deque([(y, x)])
                    visited[y][x] = True
                    
                    while q:
                        cur_y, cur_x = q.popleft()
                    
                        for i in range(4):
                            nx = cur_x + dx[i]
                            ny = cur_y + dy[i]

                            is_valid_loc = (0 <= nx < n) and (0 <= ny < n)
                            if not is_valid_loc or visited[ny][nx]:
                                continue
                            
                            diff = abs(board[cur_y][cur_x] - board[ny][nx])
                            is_able_union = l <= diff <= r
                            if not is_able_union:
                                continue
                            
                            stop_flag = False
                            
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            
                            union_blocks.append((ny, nx))
                            block_sum += board[ny][nx]
                            
                    people = math.floor(block_sum / len(union_blocks))
                    while union_blocks:
                        cur_y, cur_x = union_blocks.popleft()
                        board[cur_y][cur_x] = people
        
        if stop_flag:
            break
        ans += 1
        
    print(ans)

if __name__ == '__main__':
    main()
