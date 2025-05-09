# 집합의 표현 https://www.acmicpc.net/problem/1717

def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        root_x = find(a)
        root_y = find(b)
        if root_x != root_y:
            parent[root_y] = root_x

    for i in range(m):
        x, a, b = map(int, input().split())
        if x == 0:
            union(a, b)
        elif x == 1:
            print("YES" if find(a) == find(b) else "NO")

if __name__ == '__main__':
    main()
