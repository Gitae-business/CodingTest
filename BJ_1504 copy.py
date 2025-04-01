import heapq
from collections import defaultdict

INF = float('inf')

def dijkstra(start, graph):
    dist = [INF] * (N+1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, cur = heapq.heappop(heap)

        if (cost > dist[cur]): continue

        for next_cost, next in graph[cur]:  # 다음 노드들을 확인
            new_cost = cost + next_cost
            if new_cost < dist[next]:   # 더 짧은 경로 발견 시
                dist[next] = new_cost   # 코스트 업데이트
                heapq.heappush(heap, (new_cost, next)) # 힙에 추가

    return dist # start 노드로부터의 다른 노드들까지의 코스트가 담긴 리스트

def main():
    global N
    N, E = map(int, input().split())
    graph = defaultdict(list)  # 튜플 (cost, node)에 대한 리스트를 저장할 딕셔너리

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    u, v = map(int, input().split())
    
    # 1에서 N까지 이동해야 함. 단 u와 v를 반드시 거쳐야함
    '''
    2가지 경우가 있음
    1) 1 -> u -> v -> N
    2) 1 -> v -> u -> N
    '''

    # 음의 간선 존재 X, 재방문 가능
    # 벨만 포드 말고 다익스트라 사용. 1, u, v 확인
    d_1 = dijkstra(1, graph)
    d_u = dijkstra(u, graph)
    d_v = dijkstra(v, graph)
    
    c1 = d_1[u] + d_u[v] + d_v[N]
    c2 = d_1[v] + d_v[u] + d_u[N]
    ans = min(c1, c2)

    print(ans if ans < INF else -1)

if __name__ == '__main__':
    main()
