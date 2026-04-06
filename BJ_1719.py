# 택배 https://www.acmicpc.net/problem/1719
import sys
input = sys.stdin.readline
INF = float('inf')

def main():
    n, m = map(int, input().split())

    cost = [[INF] * (n + 1) for _ in range(n + 1)]
    first_visit = [[0] * (n + 1) for _ in range(n + 1)]    # next[i][j] = i에서 j로 갈 때 가장 먼저 방문해야 하는 노드

    for i in range(1, n+1):
        cost[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())

        cost[a][b] = c
        cost[b][a] = c

        first_visit[a][b] = b
        first_visit[b][a] = a
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    first_visit[i][j] = first_visit[i][k]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(first_visit[i][j] if i != j else '-', end=' ')
        print()


if __name__ == '__main__':
    main()
