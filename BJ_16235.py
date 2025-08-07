# 나무 재테크 https://www.acmicpc.net/problem/16235

def spring(n, nutrients, trees, dead_trees):
    for y in range(n):
        for x in range(n):
            if not trees[y][x]:
                continue
            
            trees[y][x].sort()
            alive = []
            
            for i in range(len(trees[y][x])):
                age = trees[y][x][i]
                if nutrients[y][x] >= age:
                    nutrients[y][x] -= age
                    alive.append(age + 1)
                else:
                    dead_trees[y][x].extend(trees[y][x][i:])
                    break
            
            trees[y][x] = alive

def summer(n, nutrients, dead_trees):
    for y in range(n):
        for x in range(n):
            for age in dead_trees[y][x]:
                nutrients[y][x] += age // 2
            dead_trees[y][x].clear()

def fall(n, trees):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    new_trees_to_add = []

    for y in range(n):
        for x in range(n):
            for age in trees[y][x]:
                if age % 5 == 0:
                    for d in range(8):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < n and 0 <= nx < n:
                            new_trees_to_add.append((ny, nx))
    
    for ny, nx in new_trees_to_add:
        trees[ny][nx].append(1)

def winter(n, A, nutrients):
    for y in range(n):
        for x in range(n):
            nutrients[y][x] += A[y][x]

def main():
    n, m, k = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(n)]
    nutrients = [[5] * n for _ in range(n)]
    trees = [[[] for _ in range(n)] for _ in range(n)]
    dead_trees = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        r, c, age = map(int, input().split())
        trees[r - 1][c - 1].append(age)

    for _ in range(k):
        spring(n, nutrients, trees, dead_trees)
        summer(n, nutrients, dead_trees)
        fall(n, trees)
        winter(n, A, nutrients)

    result = 0
    for y in range(n):
        for x in range(n):
            result += len(trees[y][x])

    print(result)

if __name__ == '__main__':
    main()