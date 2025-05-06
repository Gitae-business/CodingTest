from collections import deque

STD = 500

def main():
    n = int(input())
    board = [[-1] * 1001 for _ in range(1001)]

    # x1, y1, x2, y2
    points = [list(map(int, input().split())) for _ in range(n)]

    # 부모 찾기
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root
    
    # 사각형
    for i, (x1, y1, x2, y2) in enumerate(points):
        x1 += STD; x2 += STD; y1 += STD; y2 += STD

        # 상하 테두리
        for x in range(x1, x2 + 1):
            for y in (y1, y2):
                if board[y][x] != -1:
                    union(i, board[y][x])
                board[y][x] = i

        # 좌우 테두리
        for y in range(y1 + 1, y2):  # 모서리 중복 방지
            for x in (x1, x2):
                if board[y][x] != -1:
                    union(i, board[y][x])
                board[y][x] = i
    
    root_set = set(find(i) for i in range(n))

    if board[STD][STD] != -1:
        zero_root = find(board[STD][STD])
        root_set.discard(zero_root)

    print(len(root_set))

if __name__ == '__main__':
    main()
