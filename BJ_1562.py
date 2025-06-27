# 계단 수 https://www.acmicpc.net/problem/1562
MOD = 1000000000

def main():
    n = int(input())
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for length in range(1, n):
        for lastDigit in range(10):
            for mask in range(1024):
                count = dp[length][lastDigit][mask]
                if count == 0:
                    continue

                for nextDigit in [lastDigit - 1, lastDigit + 1]:
                    if 0 <= nextDigit <= 9:
                        nextMask = mask | (1 << nextDigit)
                        dp[length + 1][nextDigit][nextMask] += count
                        dp[length + 1][nextDigit][nextMask] %= MOD
    
    answer = 0
    fullMask = 1023

    for lastDigit in range(10):
        answer += dp[n][lastDigit][fullMask]
        answer %= MOD

    print(answer)

if __name__ == '__main__':
    main()
