# 운동 https://www.acmicpc.net/problem/1956
INF = float('inf')

def main():
    v, e = map(int, input().split())
    cost = [[INF for _ in range(v+1)] for _ in range(v+1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        cost[a][b] = min(cost[a][b], c)

    for z in range(1, v+1):
        for x in range(1, v+1):
            for y in range(1, v+1):
                cost[x][y] = min(cost[x][y], cost[x][z] + cost[z][y])

    answer = -1
    for i in range(1, v+1):
        if cost[i][i] != INF:
            if answer == -1:
                answer = cost[i][i]
            else:
                answer = min(answer, cost[i][i])
    print(answer)

if __name__ == '__main__':
    main()
