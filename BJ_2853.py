def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    arr = [int(input()) for _ in range(N)]
    visited = [False] * N
    boat = 0

    for i in range(1, N):
        if visited[i]:
            continue

        d = arr[i] - arr[0]
        if d == 0:
            continue  # 무의미한 간격은 스킵

        temp = 0
        for j in range(1, N):
            if not visited[j] and (arr[j] - 1) % d == 0:
                visited[j] = True
                temp += 1

        if temp > 0:
            boat += 1

    print(boat)

if __name__ == "__main__":
    main()
