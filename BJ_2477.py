# 참외밭 https://www.acmicpc.net/problem/2477
def main():
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(6)]

    points = []
    x, y = [], []
    cur_x, cur_y = 0, 0

    for d, l in arr:
        if (d == 1):    # 동
            cur_x += l
            x.append(cur_x)
        elif (d == 2):  # 서
            cur_x -= l
            x.append(cur_x)
        elif (d == 3):  # 남
            cur_y -= l
            y.append(cur_y)
        else:           # 북
            cur_y += l
            y.append(cur_y)
        points.append((cur_x, cur_y))

    points.sort()
    x.sort()
    y.sort()    

    for tx in [x[0], x[2]]:
        for ty in [y[0], y[2]]:
            if (tx, ty) not in points:
                # 전체 크기
                big = (x[2] - x[0]) * (y[2] - y[0])
                small = abs(x[1] - tx) * abs(y[1] - ty)
                print((big - small) * k)

if __name__ == '__main__':
    main()
