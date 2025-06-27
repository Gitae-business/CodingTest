# 팰린드롬 분할 https://www.acmicpc.net/problem/1509
def main():
    s = input().strip()
    n = len(s)

    palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        palindrome[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            palindrome[i][i + 1] = True

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and palindrome[i + 1][j - 1]:
                palindrome[i][j] = True

    dp = [float('inf')] * n

    for i in range(n):
        for j in range(i + 1):
            if palindrome[j][i]:
                if j == 0:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    print(dp[n - 1])

if __name__ == '__main__':
    main()
