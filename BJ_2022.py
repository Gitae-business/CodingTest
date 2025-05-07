# 사다리
import math

def main():
    x, y, c = map(float, input().split())

    '''
    두 집 사이 거리 z = a + b
    교차점 기준 수직선 내린 x축 구분 길이를 각각 a, b
    root(x^2 - z^2) : z = c : b
    root(y^2 - z^2) : z = c : a
    '''

    def solve():
        left = 0.0
        right = min(x, y)

        for _ in range(1000):
            z = (left + right) / 2
            h1 = math.sqrt(x**2 - z**2)
            h2 = math.sqrt(y**2 - z**2)
            h = (h1 * h2) / (h1 + h2)

            if h < c:
                right = z
            else:
                left = z
        return left

    ans = solve()
    print(f"{ans:.3f}")

if __name__ == '__main__':
    main()
