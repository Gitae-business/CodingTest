INF = int(1e9)

def main():
    n, k = map(int, input().split())
    s = set()
    for _ in range(n):
        s.add(int(input()))
    coins = sorted(list(s))

    dp = [INF] * (k+1)   # dp[i]는 i원을 만드는 비용
    dp[0] = 0
    
    """
    점화식
    dp[i] = min(dp[i], dp[i-c] + 1)
    i원을 만드는 비용은 i-c원을 만드는 비용 +1 또는 현재 비용의 최솟값
    """

    for c in coins:
        for i in range(c, k + 1):
            dp[i] = min(dp[i], dp[i-c] + 1)
    
    print(dp[k] if dp[k] != INF else -1)

if __name__ == '__main__':
    main()
