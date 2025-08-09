# 환승 https://www.acmicpc.net/problem/5214
from collections import deque, defaultdict

def main():
    n, k, m = map(int, input().split())
    graph = defaultdict(list)
    
    for i in range(1, m + 1):
        stations = list(map(int, input().split()))
        hyperloop_node = n + i
        
        for station in stations:
            graph[station].append(hyperloop_node)
            graph[hyperloop_node].append(station)

    dist = [-1] * (n + m + 1)
    queue = deque()

    queue.append(1)
    dist[1] = 1

    while queue:
        current_node = queue.popleft()
        
        if current_node == n:
            print(dist[n])
            return

        for next_node in graph[current_node]:
            if dist[next_node] == -1:
                if next_node <= n:
                    dist[next_node] = dist[current_node] + 1
                else:
                    dist[next_node] = dist[current_node]
                queue.append(next_node)

    print(-1)

if __name__ == '__main__':
    main()