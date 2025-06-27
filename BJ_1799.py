# 비숍 https://www.acmicpc.net/problem/1799
dir = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

def Main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    usedSum = [False] * (2 * n)
    usedDiff = [False] * (2 * n)

    maxCount = [0, 0]  # [black, white]

    def Dfs(index, count, color, cells):
        if index == len(cells):
            maxCount[color] = max(maxCount[color], count)
            return

        x, y = cells[index]
        sumIndex = x + y
        diffIndex = x - y + (n - 1)

        if not usedSum[sumIndex] and not usedDiff[diffIndex]:
            usedSum[sumIndex] = True
            usedDiff[diffIndex] = True

            Dfs(index + 1, count + 1, color, cells)

            usedSum[sumIndex] = False
            usedDiff[diffIndex] = False

        Dfs(index + 1, count, color, cells)

    blackCells = []
    whiteCells = []

    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                if (x + y) % 2 == 0:
                    blackCells.append((x, y))
                else:
                    whiteCells.append((x, y))

    Dfs(0, 0, 0, blackCells)
    Dfs(0, 0, 1, whiteCells)

    print(maxCount[0] + maxCount[1])

if __name__ == '__main__':
    Main()