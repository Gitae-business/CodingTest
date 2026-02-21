# 도로포장 https://www.acmicpc.net/problem/1162
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')

def main():
    N, M, K = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dp = [[INF] * (K + 1) for _ in range(N + 1)]
    dp[1][0] = 0
    
    pq = []
    heapq.heappush(pq, (0, 1, 0))  # cost, node, cur_k
    
    while pq:
        cost, node, cur_k = heapq.heappop(pq)
        
        if cost > dp[node][cur_k]:
            continue
        
        for next_node, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < dp[next_node][cur_k]:
                dp[next_node][cur_k] = new_cost
                heapq.heappush(pq, (new_cost, next_node, cur_k))
            
            if cur_k < K and cost < dp[next_node][cur_k + 1]:
                dp[next_node][cur_k + 1] = cost
                heapq.heappush(pq, (cost, next_node, cur_k + 1))
    
    print(min(dp[N]))

if __name__ == '__main__':
    main()