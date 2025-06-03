# 1, 2, 3 더하기 4 https://www.acmicpc.net/problem/15989
def main():
    t = int(input())
    arr = [int(input()) for _ in range(t)]
    l = max(arr) + 1

    # dp[n][i]는 n을 만드는 숫자의 개수 i개란 뜻. dp[3][2]는 3을 1,2로 만드는 경우의 수
    dp = [[0 for _ in range(4)] for _ in range(l)]
    
    # 0을 만드는 경우는 none, 1개
    for i in range(1, 4):
        dp[0][i] = 1
    
    # Bottom-up
    for n in range(1, l):       # 만들 수 n
        for j in range(1, 4):   # 사용할 수 j = 1 ~ 3
            # j를 사용하지 않고 만드는 경우의 수. 1 ~ (j-1)만 사용
            dp[n][j] += dp[n][j-1]  

            # j를 사용하는 경우. n - j 경우의 수에 j만 추가
            if n - j >= 0:
                dp[n][j] += dp[n-j][j]

    for n in arr:
        print(dp[n][3])

if __name__ == '__main__':
    main()