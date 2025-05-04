INF = int(1e9)
ans = INF

def check(n, h, ladder):
    for start in range(1, n+1):
        k = start
        for y in range(1, h+1):
            if ladder[y][k]:      # 오른쪽 이동
                k += 1
            elif ladder[y][k - 1]:  # 왼쪽 이동
                k -= 1
        if k != start:
            return False
    return True

def DFS(n, h, depth, ladder, pos):
    global ans
    if depth >= ans:  # 현재보다 많으면 중단
        return
    if check(n, h, ladder):
        ans = min(ans, depth)
        return
    if depth == 3:
        return

    for i in range(pos, h * (n - 1)):
        y = i // (n - 1) + 1
        x = i % (n - 1) + 1
        if ladder[y][x] or ladder[y][x - 1] or ladder[y][x + 1]:
            continue
        ladder[y][x] = True
        DFS(n, h, depth + 1, ladder, i + 1)
        ladder[y][x] = False

def main():
    global ans
    n, m, h = map(int, input().split())
    ladder = [[False] * (n + 2) for _ in range(h + 2)]

    for _ in range(m):
        y, x = map(int, input().split())
        ladder[y][x] = True

    DFS(n, h, 0, ladder, 0)
    print(-1 if ans == INF else ans)

if __name__ == '__main__':
    main()
