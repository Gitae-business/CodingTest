# 직사각형 https://www.acmicpc.net/problem/2527
def main():
    for _ in range(4):
        ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = map(int, input().split())

        # 공통부분 없음
        if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
            print('d')
        # 점으로 만남
        elif (ax2 == bx1 and ay2 == by1) or (ax1 == bx2 and ay2 == by1) or (ax2 == bx1 and ay1 == by2) or (ax1 == bx2 and ay1 == by2):
            print('c')
        # 선분으로 만남
        elif (ax2 == bx1 or ax1 == bx2) and (ay1 < by2 and ay2 > by1) or (ay2 == by1 or ay1 == by2) and (ax1 < bx2 and ax2 > bx1):
            print('b')
        # 직사각형으로 겹침
        else:
            print('a')

if __name__ == '__main__':
    main()
