import heapq
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(n, start, branchs):
    distance = [INF] * n
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    prev = [[] for _ in range(n)]

    while pq:
        curCost, curNode = heapq.heappop(pq)

        if distance[curNode] < curCost:
            continue

        for nextCost, nextNode in branchs[curNode]:
            newCost = curCost + nextCost

            if newCost < distance[nextNode]:
                distance[nextNode] = newCost
                prev[nextNode] = [curNode]
                heapq.heappush(pq, (newCost, nextNode))
            elif newCost == distance[nextNode]:
                prev[nextNode].append(curNode)

    return distance, prev

def remove_shortest_paths(n, dest, branchs, prev):
    q = deque([dest])
    visited = [[False] * n for _ in range(n)]

    while q:
        node = q.popleft()
        for pre in prev[node]:
            if not visited[pre][node]:
                visited[pre][node] = True
                branchs[pre] = [(c, v) for (c, v) in branchs[pre] if v != node]
                q.append(pre)

def main():
    while 1:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        branchs = [[] for _ in range(n)]
        s, d = map(int, input().split())
        for _ in range(m):
            u, v, p = map(int, input().split())
            branchs[u].append((p, v))

        dist, prev = dijkstra(n, s, branchs)
        remove_shortest_paths(n, d, branchs, prev)
        dist2, _ = dijkstra(n, s, branchs)
        print(-1 if dist2[d] == INF else dist2[d])

if __name__ == '__main__':
    main()
