# Prof. Ossama https://www.acmicpc.net/problem/10696
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, X = map(int, input().split())
        print(f"Case {t}: {N % X}")

if __name__ == '__main__':
    main()
