# 라면 사기 (Small) https://www.acmicpc.net/problem/18185 
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = [0] + list(map(int, input().split())) + [0, 0]
    ans = 0

    for i in range(1, N + 1):
        if arr[i+1] > arr[i+2]:
            cnt = min(arr[i], arr[i+1] - arr[i+2])
            arr[i] -= cnt
            arr[i+1] -= cnt
            ans += cnt * 5

        cnt = min(arr[i], arr[i+1], arr[i+2])
        arr[i] -= cnt
        arr[i+1] -= cnt
        arr[i+2] -= cnt
        ans += cnt * 7

        cnt = min(arr[i], arr[i+1])
        arr[i] -= cnt
        arr[i+1] -= cnt
        ans += cnt * 5

        ans += arr[i] * 3
        arr[i] = 0

    print(ans)

if __name__ == '__main__':
    main()
