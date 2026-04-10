# 로봇 조립 https://www.acmicpc.net/problem/18116
import sys
input = sys.stdin.readline

SIZE = int(1e6 + 1)

def main():
    N = int(input())
    parent = [i for i in range(SIZE)]
    count = [1 for _ in range(SIZE)]

    def find(a):
        if parent[a] == a:
            return a
        
        parent[a] = find(parent[a])
        return parent[a]
    
    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa != pb:
            count[pa] += count[pb]
            parent[pb] = pa

    for _ in range(N):
        inp = input().split()

        if inp[0] == 'I':
            union(int(inp[1]), int(inp[2]))
        else:
            p = find(int(inp[1]))
            print(count[p])

if __name__ == '__main__':
    main()
