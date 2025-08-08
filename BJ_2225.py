# 합분해 https://www.acmicpc.net/problem/2225
MOD = 1_000_000_000

def main():
    n, k = map(int, input().split())

    dp = [[0] * (n + 1) for _ in range(k + 1)]  # dp[k][n] = dp[k][n-1] + dp[k-1][n], (k: 사용한 숫자 개수, n: 만든 숫자) 

    for i in range(n + 1):
        dp[1][i] = 1

    for i in range(2, k + 1):
        for j in range(n + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD if j > 0 else 1

    print(dp[k][n])

if __name__ == '__main__':
    main()
