# 제곱 ㄴㄴ 수 https://www.acmicpc.net/problem/1016
import sys
import math

input = sys.stdin.readline

def main():
    mn, mx = map(int, input().split())
    rng = mx - mn + 1
    is_square_multiple = [False] * rng
    count = rng

    for i in range(2, int(math.sqrt(mx)) + 1):
        sq = i * i
        start = math.ceil(mn / sq)

        for j in range(start, int(mx / sq) + 1):
            val = sq * j

            if mn <= val <= mx:
                idx = val - mn

                if not is_square_multiple[idx]:
                    is_square_multiple[idx] = True
                    count -= 1

    print(count)

if __name__ == "__main__":
    main()