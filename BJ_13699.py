# 점화식 https://www.acmicpc.net/problem/13699
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]

    print(dp[N])

if __name__ == '__main__':
    main()
