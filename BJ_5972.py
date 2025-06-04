# 택배 배송 https://www.acmicpc.net/problem/5972
import heapq
from collections import defaultdict

INF = int(1e9)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    q = []
    visited = [False for _ in range(n+1)]
    graph_cost = [INF for _ in range(n+1)]

    heapq.heappush(q, (0, 1))
    visited[1] = True
    graph_cost[1] = 0

    while q:
        cost, node = heapq.heappop(q)
        for next_cost, next_node in graph[node]:
            new_cost = cost + next_cost

            if not visited[next_node] or graph_cost[next_node] > new_cost:
                visited[next_node] = True
                graph_cost[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    print(graph_cost[n])

if __name__ == '__main__':
    main()
