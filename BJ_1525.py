# 퍼즐 https://www.acmicpc.net/problem/1525
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def main():
    start = ''
    for _ in range(3):
        row = input().split()
        for num in row:
            start += num if num != '0' else '9'  # 0을 9로 변환해서 처리

    def solve():
        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)

        while queue:
            now, cnt = queue.popleft()

            if now == '123456789':  # 목표 상태
                print(cnt)
                return

            idx = now.index('9')  # 0(=9)의 위치
            x, y = idx % 3, idx // 3

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 3 and 0 <= ny < 3:
                    nidx = ny * 3 + nx
                    new_board = list(now)
                    new_board[idx], new_board[nidx] = new_board[nidx], new_board[idx]
                    new_str = ''.join(new_board)
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, cnt + 1))

        print(-1)

    solve()

if __name__ == '__main__':
    main()
