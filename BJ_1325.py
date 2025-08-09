# 효율적인 해킹 https://www.acmicpc.net/problem/1325
from collections import defaultdict, deque

INF = int(1e9)

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    numAndScore = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)
        
    def Bfs(node):
        q = deque()
        q.append(node)
        score = 1
        
        visited = [False] * (n + 1)
        visited[node] = True
        
        while q:
            current = q.popleft()
            for next in graph[current]:
                if not visited[next]:
                    score += 1
                    q.append(next)
                    visited[next] = True
                    
        return score
    
    maxScore = -1
    for node in range(1, n + 1):
        score = Bfs(node)
        maxScore = max(maxScore, score)
        numAndScore.append((node, score))
        
    coms = [i[0] for i in numAndScore if i[1] == maxScore]
    coms.sort()
    
    print(*coms)

if __name__ == '__main__':
    main()
