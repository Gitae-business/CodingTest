# 벡터 매칭 https://www.acmicpc.net/problem/1007
import math
from itertools import combinations

INF = int(1e12)

def main():
    t = int(input())

    def get_vector(ax, ay, bx, by):
        return bx - ax, by - ay

    def get_dist(x, y):
        return math.sqrt(x ** 2 + y ** 2)

    while t:
        t -= 1
        n = int(input())
        points = [tuple(map(int, input().split())) for _ in range(n)]

        tx = sum(x for x, y in points)
        ty = sum(y for x, y in points)
        ans = INF

        for select in combinations(points, n//2):
            sx = sum(x for x, y in select)
            sy = sum(y for x, y in select)

            rx = tx - sx
            ry = ty - sy

            vx = sx - rx
            vy = sy - ry

            dist = math.sqrt(vx**2 + vy**2)
            ans = min(ans, dist)

        print(f"{ans:.12f}")

if __name__ == '__main__':
    main()
