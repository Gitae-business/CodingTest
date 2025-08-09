# 결혼식 https://www.acmicpc.net/problem/5567
from collections import defaultdict, deque

def main():
    graph = defaultdict(list)
    n = int(input())
    m = int(input())
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    answer = 0
    visited = [False] * (n + 1)
    
    q = deque()
    q.append((1, 0))    # node, depth
    visited[1] = True
    
    while q:
        current, depth = q.popleft()
        for next in graph[current]:
            if not visited[next] and depth < 2:
                visited[next] = True
                q.append((next, depth+1))
                answer += 1
                
    print(answer)

if __name__ == '__main__':
    main()
