# 수리공 항승 https://www.acmicpc.net/problem/1449
import sys
input = sys.stdin.readline

def main():
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0
    cover = 0

    for i in arr:
        while cover < i:
            ans += 1
            cover = i + L - 1
    
    print(ans)


if __name__ == '__main__':
    main()
