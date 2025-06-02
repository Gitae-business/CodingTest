# 두 박스 https://www.acmicpc.net/problem/15973
def main():
    x1_1, y1_1, x2_1, y2_1 = map(int, input().split())  # 첫 번째 박스
    x1_2, y1_2, x2_2, y2_2 = map(int, input().split())  # 두 번째 박스

    # 두 박스가 아예 겹치지 않는 경우 (NULL)
    if x2_1 < x1_2 or x2_2 < x1_1 or y2_1 < y1_2 or y2_2 < y1_1:
        print("NULL")
        return

    # 두 박스가 점에서만 만나는 경우 (POINT)
    if ((x2_1 == x1_2 or x2_2 == x1_1) and (y2_1 == y1_2 or y2_2 == y1_1)):
        print("POINT")
        return

    # 두 박스가 선에서 만나는 경우 (LINE)
    if (x2_1 == x1_2 or x2_2 == x1_1):  # 세로 변이 붙음
        if not (y2_1 <= y1_2 or y2_2 <= y1_1 or y1_1 >= y2_2 or y1_2 >= y2_1):
            print("LINE")
            return
    if (y2_1 == y1_2 or y2_2 == y1_1):  # 가로 변이 붙음
        if not (x2_1 <= x1_2 or x2_2 <= x1_1 or x1_1 >= x2_2 or x1_2 >= x2_1):
            print("LINE")
            return

    print("FACE")

if __name__ == '__main__':
    main()
