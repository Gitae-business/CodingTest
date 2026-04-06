# 잃어버린 섬 https://www.acmicpc.net/problem/34146
import sys
from collections import Counter
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    counter = Counter()

    for _ in range(N):
        counter.update(map(int, input().split()))

    odd_cnt = sum(v % 2 for v in counter.values())

    if M % 2 == 0:
        print("YES" if odd_cnt == 0 else "NO")
    else:
        print("YES" if odd_cnt <= N else "NO")

if __name__ == "__main__":
    main()