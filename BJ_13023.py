# ABCDE
global ans
ans = 0

def main():
    n, m = map(int, input().split())
    graph = {i:[] for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def DFS(node, visited, depth):
        if depth == 4:  # 최대 깊이 도달 시
            global ans
            ans = 1
            return

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                DFS(next, visited, depth + 1)
                visited[next] = False

    for start in range(n):
        visited = [False for _ in range(n)]
        visited[start] = True
        DFS(start, visited, 0)
        if ans == 1:
            break
    
    print(ans)

if __name__ == '__main__':
    main()
