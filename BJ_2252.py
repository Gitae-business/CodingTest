# 줄 세우기 https://www.acmicpc.net/problem/2252
from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    indegree = [0 for _ in range(n + 1)]    # 진입 차수

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1    # 자식인 b에 진입차수 증가

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:     # 차수가 0(루트)인 노드 추가
            q.append(i)

    while q:
        node = q.popleft()
        print(node, end=' ')

        for next in graph[node]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

if __name__ == '__main__':
    main()
