# Algebraic Teamwork https://www.acmicpc.net/problem/10270
import sys
input = sys.stdin.readline

DIV = 1e9 + 7

def main():
    dp = [-1 for _ in range(int(1e5) + 1)]
    dp[0] = 1
    dp[1] = 1

    T = int(input())
    arr = [int(input()) for _ in range(T)]

    for i in range(2, max(arr) + 1):
        dp[i] = int(dp[i-1] * i % DIV)

    for i in arr:
        print(dp[i] - 1)

if __name__ == '__main__':
    main()
