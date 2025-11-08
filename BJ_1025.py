# 제곱수 찾기 https://www.acmicpc.net/problem/1025
def main():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    answer = -1

    def IsInBoard(y, x):
        return 0 <= y < n and 0 <= x < m

    for sy in range(n):
        for sx in range(m):
            val0 = int(board[sy][sx])
            r0 = int(val0 ** 0.5)
            if r0 * r0 == val0:
                answer = max(answer, val0)

            for dy in range(-n + 1, n):
                for dx in range(-m + 1, m):
                    if dx == 0 and dy == 0:
                        continue

                    num = ''
                    y, x = sy, sx

                    while IsInBoard(y, x):
                        num += board[y][x]
                        val = int(num)
                        sqrt = int(val ** 0.5)

                        if sqrt * sqrt == val:
                            answer = max(answer, val)

                        y += dy
                        x += dx

    print(answer)

if __name__ == '__main__':
    main()