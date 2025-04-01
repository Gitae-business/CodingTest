from collections import deque

def DFS(x, y, arr, visited):
    global ans

    visited[y][x] = True
    

    return

def main():
    global N, ans
    N = int(input())
    ans = 0
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    visited = [[False] * N for _ in range(N)]
    

if __name__ == '__main__':
    main()
