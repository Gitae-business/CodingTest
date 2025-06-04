# 백도어 https://www.acmicpc.net/problem/17396
import heapq
from collections import defaultdict
INF = float('inf')

def main():
    graph = defaultdict(list)
    n, m = map(int, input().split())
    sight = list(map(int, input().split()))

    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((t, b))
        graph[b].append((t, a))
    
    q = []
    graph_cost = [INF for _ in range(n)]

    heapq.heappush(q, (0, 0))
    graph_cost[0] = 0

    while q:
        time, current = heapq.heappop(q)
        if graph_cost[current] < time:
            continue

        for next_time, next in graph[current]:
            if sight[next] == 1 and next != n-1:
                continue

            new_time = time + next_time
            if graph_cost[next] > new_time:
                graph_cost[next] = new_time
                heapq.heappush(q, (new_time, next))

    print(-1 if graph_cost[n-1] == INF else graph_cost[n-1])

if __name__ == '__main__':
    main()
