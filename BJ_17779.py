# 게리맨더링 2 https://www.acmicpc.net/problem/17779
import sys
input = sys.stdin.readline
INF = int(1e9)

def main():
    n = int(input())
    a = [list(map(int, input().split(' '))) for _ in range(n)]

    answer = INF

    def div_area():
        for i in range(n):
            for j in range(n):
                x, y = i, j
                for d1 in range(1, n - 1):
                    for d2 in range(1, n - 1):
                        area = [[0] * n for _ in range(n)]
                        if 1 <= x + 1 < x + 1 + d1 + d2 <= n and 1 <= y + 1 - d1 < y + 1 < y + 1 + d2 <= n:
                            for k in range(d1 + 1):
                                area[x + k][y - k] = 5
                            for k in range(d2 + 1):
                                area[x + k][y + k] = 5
                            for k in range(d2 + 1):
                                area[x + d1 + k][y - d1 + k] = 5
                            for k in range(d1 + 1):
                                area[x + d2 + k][y + d2 - k] = 5

                            for r in range(n):
                                for c in range(n):
                                    if 1 <= r + 1 < x + 1 + d1 and 1 <= c + 1 <= y + 1:
                                        if area[r][c] != 0:
                                            continue
                                        area[r][c] = 1
                                    elif 1 <= r + 1 <= x + 1 + d2 and y + 1 < c + 1 <= n:
                                        if area[r][c] != 0:
                                            continue
                                        area[r][c] = 2
                                    elif x + 1 + d1 <= r + 1 <= n and 1 <= c + 1 < y + 1 - d1 + d2:
                                        if area[r][c] != 0:
                                            continue
                                        area[r][c] = 3
                                    elif x + 1 + d2 < r + 1 <= n and y + 1 - d1 + d2 <= c + 1 <= n:
                                        if area[r][c] != 0:
                                            continue
                                        area[r][c] = 4

                            for r in range(n):
                                if area[r].count(5) < 2 :
                                    continue
                                five_check = False
                                cnt = 0
                                for c in range(n):
                                    if area[r][c] == 5:
                                        five_check = True
                                        cnt += 1
                                        if cnt == 2:
                                            five_check = False
                                        continue
                                    if five_check:
                                        area[r][c] = 5


                            min_people(area)


    def min_people(area: list):
        nonlocal answer
        area_people = [0] * 5

        for i in range(n):
            for j in range(n):
                if area[i][j] == 1:
                    area_people[0] += a[i][j]
                if area[i][j] == 2:
                    area_people[1] += a[i][j]
                if area[i][j] == 3:
                    area_people[2] += a[i][j]
                if area[i][j] == 4:
                    area_people[3] += a[i][j]
                if area[i][j] == 5:
                    area_people[4] += a[i][j]

        min_area = min(area_people)
        max_area = max(area_people)

        answer = min(answer, max_area - min_area)


    div_area()
    print(answer)

if __name__ == '__main__':
    main()
