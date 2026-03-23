# 볶음밥 지키기 https://www.acmicpc.net/problem/30891
import sys
import math

input = sys.stdin.readline

def main():
    N, R = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = -1
    ans = (0, 0)

    for x in range(-100, 101):
        for y in range(-100, 101):
            temp_cnt = 0
            for px, py in points:
                if math.dist((x, y), (px, py)) <= R:
                    temp_cnt += 1
            
            if temp_cnt > max_cnt:
                max_cnt = temp_cnt
                ans = (x, y)

    print(f"{ans[0]} {ans[1]}")

if __name__ == '__main__':
    main()