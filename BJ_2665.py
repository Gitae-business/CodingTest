# 미로만들기 https://www.acmicpc.net/problem/2665
import heapq
INF = int(1e9)

def main():
    n = int(input())
    arr = []    # 검은 방 0, 흰 방 1. 흰 방으로만 이동 가능
    for _ in range(n):
        s = input()
        t = [int(i) for i in s]
        arr.append(t)
        
    cost = [[INF] * n for _ in range(n)]

    def BFS():
        pq = []
        heapq.heappush(pq, (1 - arr[0][0], 0, 0)) # cost, x, y

        while pq:
            c, x, y = heapq.heappop(pq)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and cost[ny][nx] == INF:
                    new_cost = c + (1 - arr[ny][nx])    # 검은 방일때 비용 1 증가
                    cost[ny][nx] = new_cost
                    if nx == n - 1 and ny == n - 1:
                        return
                    heapq.heappush(pq, (new_cost, nx, ny))

    BFS()
    print(cost[n-1][n-1])

if __name__ == '__main__':
    main()
