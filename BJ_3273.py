# 두 수의 합 https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = int(input())

    left = 0
    right = n - 1
    ans = 0

    while left < right:
        sum = arr[left] + arr[right]
        if sum > x:
            right -= 1
        else:
            if (sum == x):
                ans += 1
            left += 1
    print(ans)

if __name__ == '__main__':
    main()
