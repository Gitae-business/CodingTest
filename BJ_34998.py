# 1, 2, 3, 많다! https://www.acmicpc.net/problem/34998
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    for _ in range(N):
        solve()

def solve():
    X = int(input())
    li = list(input().split())
    
    ans = 0
    for i in range(0, 2 * X + 1, 2):
        ans += int(li[i]) if li[i] != '!' else 10
    
    print(ans if ans < 10 else '!')

if __name__ == '__main__':
    main()
