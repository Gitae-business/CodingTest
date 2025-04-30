INF = int(1e9)
ans = INF

loc = []

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

def isValid(n, x, y, visited):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n):
            return False
        if visited[ny][nx]:
            return False
    return True

def setFlower(x, y, board, visited, flag):
    cost = 0
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        visited[ny][nx] = flag
        cost += board[ny][nx]
    return cost

def DFS(n, depth, total, board, visited):
    global ans
    if depth == 3:
        ans = min(ans, total)
        return
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (isValid(n, j, i, visited)):
                cost = setFlower(j, i, board, visited, True)
                DFS(n, depth + 1, total + cost, board, visited)
                setFlower(j, i, board, visited, False)
            
def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False for _ in range(n)] for _ in range(n)]
    
    DFS(n, 0, 0, board, visited)
    print(ans)

if __name__ == '__main__':
    main()
