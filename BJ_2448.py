def draw_star(n):
    # 높이 n에 맞는 2차원 배열 생성
    canvas = [[' ' for _ in range(2 * n - 1)] for _ in range(n)]

    def fill(x, y, size):
        if size == 3:
            # 기본 삼각형 패턴
            canvas[x][y] = '*'
            canvas[x + 1][y - 1] = '*'
            canvas[x + 1][y + 1] = '*'
            for i in range(-2, 3):
                canvas[x + 2][y + i] = '*'
            return

        half = size // 2
        # 위쪽 삼각형
        fill(x, y, half)
        # 아래 왼쪽 삼각형
        fill(x + half, y - half, half)
        # 아래 오른쪽 삼각형
        fill(x + half, y + half, half)

    fill(0, n - 1, n)

    return '\n'.join(''.join(row) for row in canvas)

# 입력 및 출력
if __name__ == '__main__':
    N = int(input())
    print(draw_star(N))
