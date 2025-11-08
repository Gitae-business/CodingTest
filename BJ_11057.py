# 오르막 수 https://www.acmicpc.net/problem/11057
import sys
DIV = 10007
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [[0] * 10 for _ in range(n + 1)]

    for j in range(10):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j + 1):
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % DIV
                
    total_count = sum(dp[n]) % DIV
    
    print(total_count)

if __name__ == '__main__':
    main()