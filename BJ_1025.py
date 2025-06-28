# 제곱수 찾기 https://www.acmicpc.net/problem/1025
def main():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]

    answer = -1

    def IsInBoard(x, y):
        return 0 <= x < m and 0 <= y < n

    for sy in range(n):
        for sx in range(m):
            for dx in range(-n, n):
                for dy in range(-m, m):
                    if dx == 0 and dy == 0:
                        continue

                    num = ''
                    x, y = sx, sy

                    while IsInBoard(x, y):
                        num += board[y][x]
                        val = int(num)
                        sqrt = int(val ** 0.5)

                        if sqrt * sqrt == val:
                            answer = max(answer, val)

                        x += dx
                        y += dy

    print(answer)

if __name__ == '__main__':
    main()
