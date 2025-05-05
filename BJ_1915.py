
def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    """
    dp[y][x]는 (y, x)를 우측 하단 꼭짓점으로 하는 정사각형의 한 변의 크기
    
    점화식
    if (y, x) == 1:
        dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
    """

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                if y == 0 or x == 0:
                    dp[y][x] = 1
                else:
                    dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1

    l = 0
    for row in dp:
        l = max(*row, l)
    print(l * l)

if __name__ == '__main__':
    main()
