# Count Circle Groups
def main():
    t = int(input())
    while (t):
        t -= 1
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            root_x = find(a)
            root_y = find(b)
            if root_x != root_y:
                parent[root_y] = root_x
        
        for i in range(n):
            x1, y1, r1 = arr[i]
            for j in range(i+1, n):
                x2, y2, r2 = arr[j]

                # 통신 범위 안에 있다면
                if (r1 + r2) ** 2 >= abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2:
                    union(i, j)
        
        s = set(find(i) for i in range(n))
        print(len(s))

if __name__ == '__main__':
    main()
