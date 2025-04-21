import heapq

INF = int(1e9)

def main():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # 각 노드마다 K개의 최단거리 저장용 max-heap
    distance = [[] for _ in range(n + 1)]

    pq = []
    heapq.heappush(pq, (0, 1))  # (비용, 현재 노드)
    heapq.heappush(distance[1], 0)  # 시작 노드 비용 추가

    while pq:
        cost, node = heapq.heappop(pq)
        for next_node, next_cost in graph[node]:
            total_cost = cost + next_cost

            if len(distance[next_node]) < k:
                heapq.heappush(distance[next_node], -total_cost)
                heapq.heappush(pq, (total_cost, next_node))
            elif -distance[next_node][0] > total_cost:
                heapq.heappop(distance[next_node])
                heapq.heappush(distance[next_node], -total_cost)
                heapq.heappush(pq, (total_cost, next_node))

    # 결과 출력
    for i in range(1, n + 1):
        if len(distance[i]) < k:
            print(-1)
        else:
            print(-heapq.heappop(distance[i]))

if __name__ == '__main__':
    main()
