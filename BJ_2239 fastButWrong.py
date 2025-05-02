import heapq

origin = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

def getCands(board, x, y):
    ns = origin.copy()

    # 가로 확인
    for nx in range(9):
        ns.discard(board[y][nx])

    # 세로 확인
    for ny in range(9):
        ns.discard(board[ny][x])

    # 3x3 확인
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for ny in range(start_y, start_y + 3):
        for nx in range(start_x, start_x + 3):
            ns.discard(board[ny][nx])

    return ns

def findMinCands(board, visited):
    pq = []
    for y in range(9):
        for x in range(9):
            if visited[y][x]:
                continue
            cands = getCands(board, x, y)
            heapq.heappush(pq, (len(cands), cands, (x, y)))

    if len(pq) == 0:
        return None, (0, 0)

    _, cands, pos = heapq.heappop(pq)
    return cands, pos

def DFS(board, visited):
    cands, (x, y) = findMinCands(board, visited)
    if cands is None:
        return True  # 모든 칸 채움

    if len(cands) == 0:
        return False  # 잘못된 경로

    for c in cands:
        board[y][x] = c
        visited[y][x] = True

        if DFS(board, visited):
            return True

        board[y][x] = 0
        visited[y][x] = False

    return False  # 모든 후보 실패

def main():
    board = []
    visited = [[False for _ in range(9)] for _ in range(9)]
    for _ in range(9):
        s = input()
        row = [int(ch) for ch in s]
        board.append(row)

    for y in range(9):
        for x in range(9):
            if board[y][x] != 0:
                visited[y][x] = True

    DFS(board, visited)

    for row in board:
        print(''.join(map(str, row)))

if __name__ == '__main__':
    main()
