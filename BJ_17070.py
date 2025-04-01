# DFS 방식은 시간 초과가 발생해 DP로 풀이 방법 전환
# 방향은 가로를 0으로 잡고 시계방향 45도마다 1 증가

"""
Bottom-Up 사용

점화식은 다음과 같이 나타낼 수 있음
d=0(가로): dp[y][x][0] <-- dp[y][x-1][0], dp[y][x-1][1]
d=1(대각): dp[y][x][1] <-- dp[y-1][x-1][0], dp[y-1][x-1][1], dp[y-1][x-1][2]
d=2(세로): dp[y][x][2] <-- dp[y-1][x][2], dp[y-1][x][1]
"""

def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

    dp[0][1][0] = 1

    for y in range(N):
        for x in range(2, N):
            if arr[y][x] == 1: continue # 장애물 확인

            # 가로 방향
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][1] if arr[y][x-1] == 0 else 0

            # 세로 방향
            if (y>0) and (arr[y-1][x] == 0):
                dp[y][x][2] = dp[y-1][x][2] + dp[y-1][x][1]
            
            # 대각선 방향(x를 2부터 확인하므로 추가적인 조건 확인 필요 없음)
            if (y>0) and (arr[y][x-1] == 0) and (arr[y-1][x-1] == 0) and (arr[y-1][x] == 0):
                dp[y][x][1] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

    ans = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
    print(ans)

if __name__ == '__main__':
    main()
