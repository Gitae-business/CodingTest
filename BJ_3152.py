import heapq
from bisect import bisect_left

def main():
    n = list(map(int, input().split()))
    p = n[0]
    n = n[1:]

    LIM = max(n)
    pq = []
    heapq.heappush(pq, 1)
    nodes = []

    while(pq):
        now = heapq.heappop(pq)
        if (now > LIM): break
        nodes.append(now)

        heapq.heappush(pq, now * p)
        heapq.heappush(pq, now * p + 1)
    
    dict = {}
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            s = nodes[i] + nodes[j]
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] += 1

    ans = []
    for i in n:
        ans.append(1 if (i in dict and dict[i] == 1) else 0)
    print(*ans)

if __name__ == '__main__':
    main()
