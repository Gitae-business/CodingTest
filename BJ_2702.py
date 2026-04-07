# 초6 수학 https://www.acmicpc.net/problem/2702
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        solve()

def solve():
    a, b = map(int, input().split())
    k = gcd(a, b)
    print(int(a * b / k), k)

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    if a % b == 0:
        return b
    return gcd(b, a % b)

if __name__ == '__main__':
    main()
