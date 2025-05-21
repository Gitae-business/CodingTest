# 민호와 강호 https://www.acmicpc.net/problem/11662
import math

def main():
    ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

    def getDist(x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # 삼분 탐색을 이용한 최소 거리 구하기
    def ternary_search():
        left = 0.0
        right = 1.0
        for _ in range(100):  # 충분히 많은 반복으로 정밀하게 접근
            m1 = (2 * left + right) / 3
            m2 = (left + 2 * right) / 3

            # m1 비율에 따른 위치 계산
            Ax1 = ax + (bx - ax) * m1
            Ay1 = ay + (by - ay) * m1
            Bx1 = cx + (dx - cx) * m1
            By1 = cy + (dy - cy) * m1

            # m2 비율에 따른 위치 계산
            Ax2 = ax + (bx - ax) * m2
            Ay2 = ay + (by - ay) * m2
            Bx2 = cx + (dx - cx) * m2
            By2 = cy + (dy - cy) * m2

            dist1 = getDist(Ax1, Ay1, Bx1, By1)
            dist2 = getDist(Ax2, Ay2, Bx2, By2)

            if dist1 < dist2:
                right = m2
            else:
                left = m1

        # 최종 최소 거리 계산
        mid = (left + right) / 2
        Ax = ax + (bx - ax) * mid
        Ay = ay + (by - ay) * mid
        Bx = cx + (dx - cx) * mid
        By = cy + (dy - cy) * mid
        return getDist(Ax, Ay, Bx, By)

    result = ternary_search()
    print(f"{result:.10f}")

if __name__ == '__main__':
    main()
