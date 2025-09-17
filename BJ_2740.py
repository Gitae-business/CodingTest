# 행렬 곱셈 https://www.acmicpc.net/problem/2740
def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]

    C = [[0] * K for _ in range(N)]

    for i in range(N):
        for j in range(K):
            for l in range(M):
                C[i][j] += A[i][l] * B[l][j]

    for row in C:
        print(*row)

if __name__ == '__main__':
    main()
