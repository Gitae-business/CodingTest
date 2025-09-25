# IF문 좀 대신 써줘 https://www.acmicpc.net/problem/19637
import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    title = {}
    divides = []

    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if num in title:
            continue

        divides.append(num)
        title[num] = name

    divides.sort()
    
    for _ in range(M):
        n = int(input())
        idx = bisect_left(divides, n)
        print(title[divides[idx]])

if __name__ == '__main__':
    main()
