from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def countCheese(arr):
    temp = 0
    for row in arr:
        for c in row:
            if c: temp += 1
    return temp

def checkOutside(arr, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((0,0)) # (x, y)
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if (nx>=0 and nx<m and ny>=0 and ny<n):
                if not visited[ny][nx] and not arr[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))
    
    return visited

def melt(arr, visited, n, m):
    q = deque()

    for i in range(1,n-1):
        for j in range(1,m-1):
            if not arr[i][j]: continue

            cnt = 0
            for d in range(4):
                nx = j + dx[d]
                ny = i + dy[d]
                if visited[ny][nx]:
                    cnt += 1

            if (cnt >= 2):
                q.append((j, i))

    while q:
        x, y = q.popleft()
        arr[y][x] = False

    return arr

def main():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    while (countCheese(board) > 0):
        ans += 1
        visited = checkOutside(board, n, m)
        board = melt(board, visited, n, m)

    print(ans)

if __name__ == '__main__':
    main()
