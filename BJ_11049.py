# 행렬 곱셈 순서 https://www.acmicpc.net/problem/11049
def main():
    n = int(input())
    p = []

    for _ in range(n):
        a, b = map(int, input().split())
        if not p:
            p.append(a)
        p.append(b)
    
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):       # l: 구간 길이
        for i in range(n - l + 1):  # i: 시작 인덱스
            j = i + l - 1           # j: 종료 인덱스
            dp[i][j] = float('inf')

            for k in range(i, j):
                leftCost = dp[i][k]
                rightCost = dp[k + 1][j]
                thisCost = p[i] * p[k + 1] * p[j + 1]

                totalCost = leftCost + rightCost + thisCost 
                dp[i][j] = min(dp[i][j], totalCost)
    
    print(dp[0][n - 1])

if __name__ == '__main__':
    main()
