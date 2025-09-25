# 진우의 달 여행 (Small) https://www.acmicpc.net/problem/17484
import sys
input = sys.stdin.readline
INF = int(1e9)
DIR = [-1, 0, 1]     # 좌하단, 하단, 우하단 방향을 각각 -1, 0, 1로 정의

def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)] 
    for x in range(M):
        for i in range(3):
            dp[0][x][i] = board[0][x]

    for y in range(1, N):
        for x in range(M):
            for current_dir_idx in range(3):       
                past_x = x - DIR[current_dir_idx]
                if not (0 <= past_x < M):
                    continue

                min_past_fuel = INF
                for past_dir_idx in range(3):
                    if past_dir_idx != current_dir_idx:
                        min_past_fuel = min(min_past_fuel, dp[y-1][past_x][past_dir_idx])
                
                if min_past_fuel != INF:
                    dp[y][x][current_dir_idx] = board[y][x] + min_past_fuel

    min_fuel = INF
    for x in range(M):
        min_fuel = min(min_fuel, min(dp[N-1][x]))

    print(min_fuel)

if __name__ == '__main__':
    main()