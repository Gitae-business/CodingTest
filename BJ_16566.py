# 카드 게임 https://www.acmicpc.net/problem/16566
import sys
input = sys.stdin.readline

def main():
    global parent

    N, M, K = map(int, input().split())
    candidates = list(map(int, input().split()))
    candidates.sort()
    
    parent = [0 for _ in range(N + 1)]
    i = 0
    for c in candidates:
        while i < c and i < N:
            parent[i] = c
            i += 1

    reds = list(map(int, input().split()))
    for r in reds:
        print(parent[r])
        parent[r] = parent[parent[r]]

if __name__ == '__main__':
    main()
