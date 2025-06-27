import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visited[x] = 1
    y = graph[x]

    if not visited[y]:
        dfs(y)
    elif visited[y] == 1:
        # 사이클 시작 노드로 돌아옴
        temp = y
        while temp != x:
            result += 1
            temp = graph[temp]
        result += 1

    visited[x] = 2  # 방문 종료

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - result)
