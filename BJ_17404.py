INF = int(1e9)

def main():
    n = int(input())
    rgb = [list(map(int, input().split())) for i in range(n)]
    ans = INF

    for first in range(3):
        dp = [[INF] * 3 for _ in range(n)]

        for j in range(3):
            if j == first:  # 첫번째 집 초기화
                dp[0][j] = rgb[0][j]
            else:
                dp[0][j] = INF
        
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

        # 마지막 집은 첫 집과 색이 달라야 함
        for last in range(3):
            if last != first:
                ans = min(ans, dp[n-1][last])
            
    print(ans)

if __name__ == '__main__':
    main()
