# 사이클 게임 https://www.acmicpc.net/problem/20040

def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n)]  # 부모 노드

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 경로 압축
            x = parent[x]
        return x

    def union(a, b):
        root_x = find(a)
        root_y = find(b)
        if root_x != root_y:
            parent[root_y] = root_x
        return

    for i in range(m):
        u, v = map(int, input().split())
        # 각 노드들의 루트를 비교. 동일하다면 사이클 발생
        if find(u) == find(v):
            print(i+1)
            return
        union(u, v) # 루트 통합

    print(0)    # 사이클 발생 X 시 0 출력

if __name__ == '__main__':
    main()
