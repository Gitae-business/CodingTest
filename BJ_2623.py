# 음악프로그램 https://www.acmicpc.net/problem/2623
from collections import deque

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split()))[1:] for _ in range(m)]
    
    graph = [set() for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for row in arr:
        for i in range(1, len(row)):
            a = row[i - 1]
            b = row[i]
            if b not in graph[a]:
                graph[a].add(b)
                indegree[b] += 1

    dq = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    answer = []
    while dq:
        cur = dq.popleft()
        answer.append(cur)
        for next in graph[cur]:
            indegree[next] -= 1
            if indegree[next] == 0:
                dq.append(next)

    if len(answer) != n:
        print(0)
    else:
        [print(i) for i in answer]


"""
<위상정렬>
1. 모든 노드 진입차수 계산
2. 진입차수 0인 노드 큐에 삽입
3. 큐에서 노드 꺼내며 해당 노드 제거 및 연결된 노드 진입 차수 감소
4. 새롭게 진입 차수 0이 된 노드를 큐에 삽입
5. 큐가 빌 때까지 반복
"""

if __name__ == '__main__':
    main()
