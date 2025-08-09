# 숨바꼭질 https://www.acmicpc.net/problem/6118
from collections import defaultdict
import heapq

INF = int(1e9)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    cost = [INF] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    cost[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1)) # cost, node
    
    while pq:
        c, n = heapq.heappop(pq)
        for next in graph[n]:
            if cost[next] > c + 1:
                cost[next] = c + 1
                heapq.heappush(pq, (c + 1, next))
    
    mx = max(cost[1:])
    candidates = [idx for idx, score in enumerate(cost) if score == mx]
    
    print(candidates[0], mx, len(candidates))

if __name__ == '__main__':
    main()
