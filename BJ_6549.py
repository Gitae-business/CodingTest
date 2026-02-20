# 히스토그램에서 가장 큰 직사각형 https://www.acmicpc.net/problem/6549
import sys
input = sys.stdin.readline

def solve(arr):
    stack = []
    mx = 0
    arr.append(0)
    n = len(arr)

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]

            if stack:
                w = i - stack[-1] - 1
            else:
                w = i
        
            mx = max(mx, h * w)
        stack.append(i)
    print(mx)


def main():
    while 1:
        arr = list(map(int, input().split()))
        n = arr[0]
        if n == 0:
            break
        arr = arr[1:]

        solve(arr)

if __name__ == '__main__':
    main()
