# 인간-컴퓨터 상호작용 https://www.acmicpc.net/problem/16139
import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    S = input().strip()
    N = len(S)
    q = int(input())
    
    prefix = defaultdict(int)
    arr = [None] * N

    for i in range(N):
        prefix[S[i]] += 1
        arr[i] = prefix.copy()

    for i in range(q):
        t = input().split()
        c = t[0]
        l = int(t[1])
        r = int(t[2])

        rc = arr[r][c]
        lc = arr[l-1][c]

        print(rc - (lc if l-1 >=0 else 0))

if __name__ == '__main__':
    main()
