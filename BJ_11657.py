# 타임머신 https://www.acmicpc.net/problem/11657
INF = float('inf')

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    dist = [INF for _ in range(n + 1)]
    
    start = 1
    dist[start] = 0

    def bellmanFord():
        for _ in range(1, n+1):
            for a, b, c in edges:
                if dist[a] != INF and dist[b] > dist[a] + c:
                    dist[b] = dist[a] + c
        
        # 음수 사이클 검사
        for a, b, c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                return False
            
        return True
    
    if not bellmanFord():
        print(-1)
    else:
        for i in dist[2:]:
            print(i if i != INF else -1)
    

if __name__ == '__main__':
    main()
