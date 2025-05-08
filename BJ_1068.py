# 트리 https://www.acmicpc.net/problem/1068
cnt = 0

def main():
    n = int(input())
    parent = list(map(int, input().split()))
    toDel = int(input())
    
    graph = {i:[] for i in range(n)}
    root = -1
    for i in range(n):
        if parent[i] == -1:     # 루트 노드
            root = i
            continue
        if i == toDel:          # 제거할 노드
            continue
        graph[parent[i]].append(i)

    # root를 제거하면 0 출력
    if toDel == root:
        print(0)
        return

    # DFS로 리프 탐색
    visited = [False for _ in range(n)]
    def DFS(node):
        global cnt
        if len(graph[node]) == 0:
            cnt += 1
            return

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                DFS(next)
        
        return

    DFS(root)
    print(cnt)

if __name__ == '__main__':
    main()
