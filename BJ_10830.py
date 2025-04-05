def matrix_mul(A, B, mod = 1000):
    n = len(A)
    res = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= mod
    return res

def matrix_pow(A, b):
    if (b == 1):    # 각 원소에 1000으로 나눈 나머지
        return [[x % 1000 for x in row] for row in A]

    half = matrix_pow(A, b // 2)
    half_sq = matrix_mul(half, half)

    if (b % 2 == 0):
        return half_sq
    else:
        return matrix_mul(half_sq, A)

def main():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    result = matrix_pow(A, B)

    for row in result:
        print(*row)

if __name__ == '__main__':
    main()
