# 전자레인지 https://www.acmicpc.net/problem/10162
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if (n % 10 != 0):
        print(-1)
        return
    
    a = n // (5 * 60)
    n %= (5 * 60)
    b = n // 60
    n %= 60
    
    print(f"{a} {b} {n // 10}")

if __name__ == '__main__':
    main()
