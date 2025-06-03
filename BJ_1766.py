# 문제집 https://www.acmicpc.net/problem/1766
import heapq

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)    # 진입 차수

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)  # A -> B
        indegree[b] += 1    # B의 진입 차수 증가
    
    pq = []
    for i in range(1, n + 1):   # 작은 노드들 부터
        if indegree[i] == 0:    # 차수가 0인 노드를 찾아
            heapq.heappush(pq, i)   # 우선순위 큐에 추가
    
    result = []
    while pq:
        current = heapq.heappop(pq)
        result.append(current)

        for next in graph[current]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(pq, next)
    
    print(*result)

if __name__ == '__main__':
    main()
