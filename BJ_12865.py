# 평범한 배낭 https://www.acmicpc.net/problem/12865
def main():
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # dp[w]: w만큼 담았을 때의 최대 가치
    dp = [0 for _ in range(k)]

    for w, v in arr:
        for i in range(k, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)

    print(dp[k])
            
if __name__ == '__main__':
    main()
