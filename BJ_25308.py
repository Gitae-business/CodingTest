# 방사형 그래프
import math
from itertools import permutations

def main():
    arr = list(map(int, input().split()))

    def CCW(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def getPoint(i, r):
        theta = math.radians(45 * i)
        return (r * math.cos(theta), r * math.sin(theta))

    def check(perm):
        prev = 0
        for i in range(8):
            p1 = getPoint(i, perm[i])
            p2 = getPoint((i + 1) % 8, perm[(i + 1) % 8])
            p3 = getPoint((i + 2) % 8, perm[(i + 2) % 8])

            z = CCW(p1, p2, p3)
            if z != 0:
                if prev == 0:       # 첫 번째 계산
                    prev = z
                elif prev * z < 0:  # 방향이 바뀌었다면
                    return False
        return True

    ans = 0
    for perm in list(permutations(arr)): # 가능한 모든 경우의 수
        if check(perm):
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
