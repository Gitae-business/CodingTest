# 중량제한 https://www.acmicpc.net/problem/1939
import heapq

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    start, end = map(int, input().split())

    graph = {i:[] for i in range(n+1)}
    for a, b, c in arr:
        # 양방향
        graph[a].append((b, c)) # (next, cost) 형식 
        graph[b].append((a, c)) 

    # start에서 해당 노드로 갈 수 있는 최대 무게
    cost = [0] * (n + 1)
    visited = [False] * (n + 1)

    q = [(float('-inf'), start)]    # 초기값은 무한. 무거운 무게를 우선으로 탐색하기 위해 음수.

    while q:
        cur_w, node = heapq.heappop(q)
        cur_w = -cur_w  # 부호 보정

        if visited[node]:
            continue
        visited[node] = True
        cost[node] = cur_w

        if node == end:
            break

        for next, weight in graph[node]:
            if not visited[next]:
                next_w = min(cur_w, weight)
                heapq.heappush(q, (-next_w, next))

    print(cost[end])

if __name__ == '__main__':
    main()
