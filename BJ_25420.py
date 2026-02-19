# 끝까지 외친 정수의 개수 https://www.acmicpc.net/problem/25420
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    invalid_num_set = set(map(int, input().split()))

    is_win = [False] * (N + 1)
    dp = [0] * (N + 1)

    for i in range(N, -1, -1):
        can_call = []

        for j in range(1, K + 1):
            next_num = i + j
            if next_num <= N and next_num not in invalid_num_set:
                can_call.append(next_num)
        
        if not can_call:
            is_win[i] = False
            dp[i] = 0
            continue
        
        win_calls = [m for m in can_call if not is_win[m]]
        
        if win_calls:
            is_win[i] = True
            dp[i] = min(dp[m] for m in win_calls) + 1
        else:
            is_win[i] = False
            dp[i] = max(dp[m] for m in can_call) + 1

    print(dp[0])

if __name__ == '__main__':
    main()
