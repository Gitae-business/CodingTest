# 대칭제곱수 https://www.acmicpc.net/problem/33573
import sys
import math
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        solve()

def solve():
    s = input().strip()
    
    a = to_num(s)
    b = to_num(reversed(s))
    
    print("YES" if check(a) and check(b) else "NO")

def to_num(s):
    res = 0
    for c in s:
        res *= 10
        res += int(c)
    return res

def check(n):
    sq = int(math.sqrt(n))
    return sq ** 2 == n

if __name__ == '__main__':
    main()
