import sys

def main():
    N, E = map(int, input().split())
    INF = sys.maxsize
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    u, v = map(int, input().split())
    
    # 1에서 N까지 이동해야 함. 단 u와 v를 반드시 거쳐야함
    '''
    2가지 경우가 있음
    1) 1 -> u -> v -> N
    2) 1 -> v -> u -> N
    '''

    # 음의 간선 존재 X, 재방문 가능
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if (graph[i][j] > graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    c_1 = graph[1][u] + graph[u][v] + graph[v][N]
    c_2 = graph[1][v] + graph[v][u] + graph[u][N]
    ans = min(c_1, c_2)

    print(ans) if ans < INF else print(-1)

if __name__ == '__main__':
    main()
