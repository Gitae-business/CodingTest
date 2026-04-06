# 해킹 https://www.acmicpc.net/problem/10282
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')

def solve():
    n, d, c = map(int, input().split())
    costs = [INF] * (n + 1)

    graph = defaultdict(list)
    costs[c] = 0

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    pq = []
    heapq.heappush(pq, (0, c))  # cost, node

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > costs[node]:
            continue

        for next_node, next_cost in graph[node]:
            next_co = cost + next_cost

            if next_co < costs[next_node]:
                costs[next_node] = next_co
                heapq.heappush(pq, (next_co, next_node))
    
    cnt = 0
    last_time = 0
    for c in costs:
        if c != INF:
            cnt += 1
            last_time = max(last_time, c)
    
    print(cnt, last_time)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
