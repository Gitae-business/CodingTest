# 역사 https://www.acmicpc.net/problem/1613
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    matrix = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        matrix[i][i] = True

    for _ in range(k):
        a, b = map(int, input().split())
        matrix[a][b] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                matrix[i][j] |= matrix[i][k] and matrix[k][j]
                
    s = int(input())
    for _ in range(s):
        a, b = map(int, input().split())
        if (matrix[a][b] and not matrix[b][a]):
            print(-1)
        elif (matrix[b][a] and not matrix[a][b]):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()
