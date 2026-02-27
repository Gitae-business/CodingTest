# Gift https://www.acmicpc.net/problem/9848
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    ans = 0
    for i in range(1, n):
        if arr[i - 1] - arr[i] >= k:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
