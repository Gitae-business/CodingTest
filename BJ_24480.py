# 알고리즘 수업 - 깊이 우선 탐색 2 https://www.acmicpc.net/problem/24480
from collections import defaultdict

def main():
    n, m, r = map(int, input().split())
    graph = defaultdict(list)
    cost = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    stack = [r]
    cnt = 1
    
    while stack:
        cur_node = stack.pop()
        
        if cost[cur_node] != 0:
            continue
            
        cost[cur_node] = cnt
        cnt += 1
        
        for next_node in sorted(graph[cur_node], reverse=False):
            if cost[next_node] == 0:
                stack.append(next_node)
    
    for i in range(1, n + 1):
        print(cost[i])

if __name__ == '__main__':
    main()