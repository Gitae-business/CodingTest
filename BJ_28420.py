# 카더가든 https://www.acmicpc.net/problem/28420
def main():
    n, m = map(int, input().split())
    a, b, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = float('inf')

    def IsInBoard(x, y):
        return 0 <= x < m and 0 <= y < n

    # 누적합 구하기
    psum = [[0] * (m + 1) for _ in range(n + 1)]
    for y in range(n):
        for x in range(m):
            psum[y + 1][x + 1] = board[y][x] + psum[y][x + 1] + psum[y + 1][x] - psum[y][x]

    def GetSum(x1, y1, x2, y2):
        return psum[y2 + 1][x2 + 1] - psum[y1][x2 + 1] - psum[y2 + 1][x1] + psum[y1][x1]

    def CheckCase1(startX, startY):
        nonlocal answer
        x2 = startX + b + c - 1
        y2 = startY + a - 1
        if not (IsInBoard(startX, startY) and IsInBoard(x2, y2)):
            return
        score = GetSum(startX, startY, x2, y2)
        answer = min(answer, score)

    def CheckCase2(startX, startY):
        nonlocal answer
        xMid = startX + c - 1
        yMid = startY + a - 1
        x2 = startX + c + a - 1
        y2 = startY + a + b - 1
        if not (IsInBoard(startX, startY) and IsInBoard(x2, y2)):
            return
        score = GetSum(startX, startY, xMid, yMid) + GetSum(xMid + 1, yMid + 1, x2, y2)
        answer = min(answer, score)

    def CheckCase3(startX, startY):
        nonlocal answer
        xMid = startX + b - 1
        yMid = startY + a - 1
        x2 = startX + b + a - 1
        y2 = startY + a + c - 1
        if not (IsInBoard(startX, startY) and IsInBoard(x2, y2)):
            return
        score = GetSum(startX, startY, xMid, yMid) + GetSum(xMid + 1, yMid + 1, x2, y2)
        answer = min(answer, score)

    for y in range(n):
        for x in range(m):
            CheckCase1(x, y)
            CheckCase2(x, y)
            CheckCase3(x, y)

    print(answer)

if __name__ == '__main__':
    main()
