# LCS https://www.acmicpc.net/problem/9251
def main():
    # 최장 공통 부분 수열
    a = input()
    b = input()

    la, lb = len(a), len(b)
    dp = [[0 for _ in range(lb + 1)] for _ in range(la + 1)]

    """
    점화식
    a[i-1]과 b[j-1] 위치의 문자가 동일하다면  dp[i][j] =  dp[i-1][j-1] + 1 
    아니라면                            max(dp[i-1][j], dp[i][j-1])
    """ 

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if a[i-1] == b[j-1] else max(dp[i-1][j], dp[i][j-1])
    
    print(dp[la][lb])

if __name__ == '__main__':
    main()
