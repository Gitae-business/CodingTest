# 벽 부수고 이동하기 4 https://www.acmicpc.net/problem/16946
import sys
from collections import defaultdict
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def main():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        s = input().strip()
        temp = []
        for char in s:
            temp.append(int(char))
        board.append(temp)

    parents = [i for i in range(N * M)] 
    costs = defaultdict(int)

    def to_node_num(y, x):
        return M * y + x

    def check_in_board(y, x):
        return 0 <= y < N and 0 <= x < M

    def find(node):
        if parents[node] == node:
            return node
        
        parents[node] = find(parents[node])
        return parents[node]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a != parent_b:
            if parent_a < parent_b:
                parents[parent_b] = parent_a
                return parent_a, parent_b
            else:
                parents[parent_a] = parent_b
                return parent_b, parent_a
        return None, None

    for y in range(N):
        for x in range(M):
            if board[y][x] != 0:
                continue
            
            n1 = to_node_num(y, x)
            
            if check_in_board(y, x + 1) and board[y][x + 1] == 0:
                n2 = to_node_num(y, x + 1)
                union(n1, n2)

            if check_in_board(y + 1, x) and board[y + 1][x] == 0:
                n2 = to_node_num(y + 1, x)
                union(n1, n2)

    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                node = to_node_num(y, x)
                root = find(node)
                costs[root] += 1

    def get_movables(y, x):
        total_movable = 1
        adjacent_roots = set() 
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if check_in_board(ny, nx) and board[ny][nx] == 0:
                node = to_node_num(ny, nx)
                root = find(node)
                adjacent_roots.add(root)

        for root in adjacent_roots:
            total_movable += costs[root]

        return total_movable % 10

    result_board = []
    for y in range(N):
        row_str = []
        for x in range(M):
            if board[y][x] == 0:
                row_str.append('0')
            else:
                row_str.append(str(get_movables(y, x)))
        result_board.append("".join(row_str))

    sys.stdout.write("\n".join(result_board) + "\n")

if __name__ == '__main__':
    main()