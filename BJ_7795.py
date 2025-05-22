# 먹을 것인가 먹힐 것인가 https://www.acmicpc.net/problem/7795
from bisect import bisect_left

def main():
    t = int(input())
    while t:
        t -= 1
        n, m = map(int, input().split())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()

        ans = 0
        for i in a:
            idx = bisect_left(b, i)
            ans += idx
        
        print(ans)


if __name__ == '__main__':
    main()
