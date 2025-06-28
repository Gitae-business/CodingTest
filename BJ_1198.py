# 삼각형으로 자르기 https://www.acmicpc.net/problem/1198
from itertools import combinations

def CalcTriangleArea(x1, y1, x2, y2, x3, y3):
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return area


def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    answer = -1

    for p in combinations(points, 3):
        area = CalcTriangleArea(p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1])
        answer = max(answer, area)

    print(answer)

if __name__ == '__main__':
    main()
