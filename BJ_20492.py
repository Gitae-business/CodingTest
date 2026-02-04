# 세금 https://www.acmicpc.net/problem/20492
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    print(int(N * 0.78), int(N - N * 0.2 * 0.22))

if __name__ == '__main__':
    main()
