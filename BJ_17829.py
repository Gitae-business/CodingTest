# 222-풀링 https://www.acmicpc.net/problem/17829
def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    def divide(x, y, size):
        if size == 2:
            vals = [
                board[y][x], board[y][x+1], board[y+1][x], board[y+1][x+1]
            ]
            vals.sort()
            return vals[-2]
        
        half = size // 2
        result = [
            divide(x, y, half),
            divide(x, y+half, half),
            divide(x+half, y, half),
            divide(x+half, y+half, half)
        ]
        result.sort()
        return result[-2]

    answer = divide(0, 0, n)
    print(answer)

if __name__ == '__main__':
    main()
