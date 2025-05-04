ans = 0

def dfs(graph, indoor, visited, node, depth):
    if depth > 2: return
    if depth > 0 and indoor[node]:
        global ans
        ans += 1
        return

    for next in graph[node]:
        if visited[next]: continue
        visited[next] = True
        dfs(graph, indoor, visited, next, depth+1)
    
    return

def main():
    n = int(input())
    indoor = [False for _ in range(n+1)]
    for i, c in enumerate(input()):
        if c == '1':
            indoor[i+1] = True
    
    graph = {i:[] for i in range(1,n+1)}
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        visited[i] = True
        if indoor[i]: dfs(graph, indoor, visited, i, 0)

    global ans
    print(ans)    


if __name__ == '__main__':
    main()
