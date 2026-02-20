# 두 용액 https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    mn = 1e12
    left = l = 0
    right = r = N - 1

    while l < r:
        sum = arr[l] + arr[r]
        if abs(sum) < abs(mn):
            mn = sum
            left = l
            right = r
        
        if abs(arr[l+1] + arr[r]) < abs(arr[l] + arr[r-1]):
            l += 1
        else:
            r -= 1

    print(arr[left], arr[right])


if __name__ == '__main__':
    main()
