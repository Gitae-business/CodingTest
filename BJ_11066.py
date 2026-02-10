# 파일 합치기 https://www.acmicpc.net/problem/11066
def main():
    T = int(input())
    for _ in range(T):
        solve()

def solve():
    K = int(input())
    arr = list(map(int, input().split()))

    prefix = [0] * (K + 1)
    for i in range(K):
        prefix[i + 1] = prefix[i] + arr[i]

    def get_cost(i, j):
        return prefix[j + 1] - prefix[i]

    dp = [[0] * K for _ in range(K)]
    opt = [[0] * K for _ in range(K)]

    for i in range(K):
        opt[i][i] = i
    
    for l in range(2, K + 1):
        for i in range(K - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')

            start = max(opt[i][j - 1], i)
            end = min(opt[i + 1][j], j - 1)

            for k in range(start, end + 1):
                value = dp[i][k] + dp[k + 1][j] + get_cost(i, j)
                if value < dp[i][j]:
                    dp[i][j] = value
                    opt[i][j] = k

    print(dp[0][K - 1])

if __name__ == '__main__':
    main()
