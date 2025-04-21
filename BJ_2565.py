from bisect import bisect_left
import heapq

def main():
    n = int(input())
    pq = []
    for _ in range(n):
        x, y = map(int, input().split())
        heapq.heappush(pq, (x, y))

    dp = []
    while pq:
        x, y = heapq.heappop(pq)
        idx = bisect_left(dp, y)

        if (idx == len(dp)):
            dp.append(y)
        else:
            dp[idx] = y

    print(n - len(dp))


if __name__ == '__main__':
    main()
