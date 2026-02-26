# 행성 터널 https://www.acmicpc.net/problem/2887
import sys
import heapq
input = sys.stdin.readline

parent = []

def main():
    global parent
    N = int(input())
    parent = [i for i in range(N)]

    planets = []
    for i in range(N):
        x, y, z = map(int, input().split())
        planets.append((x, y, z, i))

    pq = []
    
    planets.sort(key=lambda x: x[0])    # x축 정렬
    for i in range(N - 1):
        cost = abs(planets[i][0] - planets[i+1][0])
        heapq.heappush(pq, (cost, planets[i][3], planets[i+1][3]))
    
    planets.sort(key=lambda x: x[1])    # y축 정렬
    for i in range(N - 1):
        cost = abs(planets[i][1] - planets[i+1][1])
        heapq.heappush(pq, (cost, planets[i][3], planets[i+1][3]))
    
    planets.sort(key=lambda x: x[2])    # z축 정렬
    for i in range(N - 1):
        cost = abs(planets[i][2] - planets[i+1][2])
        heapq.heappush(pq, (cost, planets[i][3], planets[i+1][3]))
    
    ans = 0
    while pq:
        cost, a, b = heapq.heappop(pq)
        if find(a) != find(b):
            union(a, b)
            ans += cost
    
    print(ans)

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa

if __name__ == '__main__':
    main()
