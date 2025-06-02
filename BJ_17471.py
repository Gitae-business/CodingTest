# 게리맨더링 https://www.acmicpc.net/problem/17471
from itertools import combinations
from collections import deque

INF = int(1e9)

def main():
    n = int(input())
    people = [0] + list(map(int, input().split()))
    graph = {}
    
    for i in range(1, n+1):
        li = list(map(int, input().split()))
        graph[i] = li[1:]

    def isConnected(group):
        visited = set()
        q = deque([group[0]])
        visited.add(group[0])

        while q:
            node = q.popleft()
            for next in graph[node]:
                if (next in group) and (next not in visited):
                    visited.add(next)
                    q.append(next)
        return len(visited) == len(group)
    
    answer = INF
    for r in range(1, n // 2 + 1):
        for group_a in combinations(range(1, n+1), r):
            group_b = [i for i in range(1, n+1) if i not in group_a]

            if isConnected(group_a) and isConnected(group_b):
                sum_a = sum(people[i] for i in group_a)
                sum_b = sum(people[i] for i in group_b)
                answer = min(answer, abs(sum_a - sum_b))
    
    print(answer if answer != INF else -1)

if __name__ == '__main__':
    main()
