# 특별상이라도 받고 싶어 https://www.acmicpc.net/problem/24460
def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    def find(x, y, size):
        if size == 2:
            values = [
                board[y][x], board[y][x + 1],
                board[y + 1][x], board[y + 1][x + 1]
            ]
            values.sort()
            return values[1]

        new_size = size // 2
        top_left = find(x, y, new_size)
        top_right = find(x + new_size, y, new_size)
        bottom_left = find(x, y + new_size, new_size)
        bottom_right = find(x + new_size, y + new_size, new_size)

        results = [top_left, top_right, bottom_left, bottom_right]
        results.sort()
        
        return results[1]

    print(find(0, 0, n))

if __name__ == '__main__':
    main()
