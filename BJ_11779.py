import heapq
import math

INF = math.inf

def main():
    n = int(input())
    m = int(input())

    path = {}
    prev = {}
    for i in range(1, n+1):
        path[i] = []
        prev[i] = None

    for _ in range(m):
        s, e, c = map(int, input().split())
        path[s].append((c, e))
    
    start, end = map(int, input().split())

    push = heapq.heappush
    pop = heapq.heappop
    q = []

    graph = [INF for _ in range(n+1)]
    graph[start] = 0

    push(q, (0, start))

    while q:
        cost, node = pop(q)
        if cost > graph[node]:
            continue

        for next in path[node]:
            nextCost, nextNode = next
            newCost = cost + nextCost

            if (newCost < graph[nextNode]):
                graph[nextNode] = newCost
                prev[nextNode] = node
                push(q, (newCost, nextNode))

    
    route = []
    n = end

    while True:
        route.append(n)
        n = prev[n]
        if (n==start): 
            route.append(start)
            route.reverse()
            break
    
    print(graph[end])
    print(len(route))
    print(*route)


if __name__ == '__main__':
    main()
