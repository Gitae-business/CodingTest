# 라면 사기 (Large) https://www.acmicpc.net/problem/18186
import sys
input = sys.stdin.readline

def main():
    N, B, C = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [0, 0]

    if B <= C:
        print(sum(arr) * B)
        return

    ans = 0

    for i in range(1, N + 1):
        if arr[i + 1] > arr[i + 2]:
            cnt = min(arr[i], arr[i + 1] - arr[i + 2])
            arr[i] -= cnt
            arr[i + 1] -= cnt
            ans += cnt * (B + C)

        cnt = min(arr[i], arr[i + 1], arr[i + 2])
        arr[i] -= cnt
        arr[i + 1] -= cnt
        arr[i + 2] -= cnt
        ans += cnt * (B + 2 * C)

        cnt = min(arr[i], arr[i + 1])
        arr[i] -= cnt
        arr[i + 1] -= cnt
        ans += cnt * (B + C)

        ans += arr[i] * B
        arr[i] = 0

    print(ans)

if __name__ == '__main__':
    main()