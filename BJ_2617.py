# 구슬 찾기 https://www.acmicpc.net/problem/2617
from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())
    answer_set = set()
    
    heavy = defaultdict(list)
    heavy_cost = [[0] * (n + 1) for _ in range(n + 1)]
    
    light = defaultdict(list)
    light_cost = [[0] * (n + 1) for _ in range(n + 1)]
    
    # HEAVY
    for _ in range(m):
        a, b = map(int, input().split())
        heavy[a].append(b)
        light[b].append(a)
        
    for start in range(1, n + 1):
        visited = [False] * (n + 1)
        visited[start] = True
        
        q = deque()
        q.append(start)
        
        while q:
            node = q.popleft()
            for next in heavy[node]:
                if not visited[next]:
                    visited[next] = True
                    heavy_cost[start][next] = 1
                    q.append(next)
        
    for i in range(1, n+1):
        cnt = sum(heavy_cost[i])
        if cnt > n // 2:
            answer_set.add(i)
    
    # LIGHT
    for start in range(1, n + 1):
        visited = [False] * (n + 1)
        visited[start] = True
        
        q = deque()
        q.append(start)
        
        while q:
            node = q.popleft()
            for next in light[node]:
                if not visited[next]:
                    visited[next] = True
                    light_cost[start][next] = 1
                    q.append(next)
        
    for i in range(1, n+1):
        cnt = sum(light_cost[i])
        if cnt > n // 2:
            answer_set.add(i)
            
    print(len(answer_set))

if __name__ == '__main__':
    main()
