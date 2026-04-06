# 거스름돈 https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0
    
    for coin in [2, 5]:
        for target in range(coin, n + 1):
            dp[target] = min(dp[target], dp[target - coin] + 1)

    print(-1 if dp[n] == INF else dp[n])

if __name__ == '__main__':
    main()
