# 냅색문제 https://www.acmicpc.net/problem/1450
import sys
from bisect import bisect_right
input = sys.stdin.readline

def get_sums(arr):
    n = len(arr)
    result = []
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += arr[i]
        result.append(total)
    return result

def main():
    N, C = map(int, input().split())
    weights = list(map(int, input().split()))

    left = weights[:N//2]
    right = weights[N//2:]

    left_sums = get_sums(left)
    right_sums = get_sums(right)

    right_sums.sort()

    answer = 0
    for l in left_sums:
        if l > C:
            continue
        remain = C - l
        answer += bisect_right(right_sums, remain)

    print(answer)

if __name__ == "__main__":
    main()