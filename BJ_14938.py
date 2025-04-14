import sys
import math
from queue import PriorityQueue

def main():
    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))   # 1부터 시작하게 하기 위해
    graph = {}

    for i in range(1, n+1):  # 각 노드를 리스트로 초기화
        graph[i] = []

    for i in range(r):  # 각 리스트에 (거리, 노드) 형태로 저장. 양방향
        a, b, l = map(int, input().split())
        graph[a].append((l, b))
        graph[b].append((l, a))
    
    # 각각의 모든 노드를 시작점으로 잡고 다익스트라 돌려서 최대값 저장해 출력
    ans = 0
    for start in range(1, n + 1):
        q = PriorityQueue()   # 최초의 우선순위큐
        q.put((0, start))

        route = [math.inf for _ in range(n + 1)] # 거리, 초기값은 inf
        route[start] = 0

        while not q.empty():    # 우선순위 큐가 빌 때까지 실행
            cost, now = q.get()
            if (cost > m):  # 탐색범위 m을 초과하면 탐색종료
                continue

            for next_cost, next_node in graph[now]:
                new_cost = cost + next_cost
                if (route[next_node] > new_cost):  # 현재의 경로가 더 짧은지 확인
                    route[next_node] = new_cost  # 경로 업데이트
                    q.put((new_cost, next_node)) # 해당 노드 재탐색


        # 시작 노드부터 각 노드까지의 거리가 m 이하인 노드들을 찾아 해당 노드의 아이템 수를 더함
        temp = 0
        for node in range(1, n+1):
            if (route[node] <= m):
                temp += items[node-1]
        ans = max(ans, temp)    # 정답 업데이트

    # 정답 출력
    print(ans)

if __name__ == '__main__':
    main()
