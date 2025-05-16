# 정사각형 https://www.acmicpc.net/problem/1485
from itertools import permutations

def dist2(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def dot(p1, p2, p3):    # 벡터 p1p2 · p1p3
    v1 = (p2[0]-p1[0], p2[1]-p1[1])
    v2 = (p3[0]-p1[0], p3[1]-p1[1])
    return v1[0]*v2[0] + v1[1]*v2[1]

def is_square(points):
    for order in permutations(points):
        A, B, C, D = order
        # AB == BC == CD == DA
        if dist2(A, B) == dist2(B, C) == dist2(C, D) == dist2(D, A):
            # 대각선 AC == BD
            if dist2(A, C) == dist2(B, D):
                # 직각 확인 (벡터 내적 0)
                if dot(A, B, D) == 0:
                    return 1
    return 0

def main():
    T = int(input())
    for _ in range(T):
        points = [tuple(map(int, input().split())) for _ in range(4)]
        print(is_square(points))

if __name__ == '__main__':
    main()
