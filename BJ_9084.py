def main():
    t = int(input())
    while (t):
        t -= 1
        n = int(input())
        coins = list(map(int, input().split())) # ASC
        m = int(input())

        dp = [0] * (m + 1)
        dp[0] = 1

        """
        점화식
        dp[i] = sum(dp[i-c] for c in coins)
        """

        for c in coins:
            for i in range(c, m + 1):
                dp[i] += dp[i - c]
        
        print(dp[m])

if __name__ == '__main__':
    main()
