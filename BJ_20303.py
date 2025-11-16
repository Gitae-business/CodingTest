# 할로윈의 양아치 https://www.acmicpc.net/problem/20303
import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N, M, K = map(int, input().split())
    candies = list(map(int, input().split()))
    parents = [i for i in range(N+1)]
    
    candies_count = defaultdict(int)
    people_count = defaultdict(int)

    def find(n):
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def union(a, b):
        pa = find(a)
        pb = find(b)

        if pa == pb:
            return
        
        if pb > pa:
            parents[pb] = pa
        else:
            parents[pa] = pb
    
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, N+1):
        p = find(i)
        candies_count[p] += candies[i-1]
        people_count[p] += 1
    
    li = []
    max_people_limit = K - 1
    
    for root in candies_count:
        candy = candies_count[root]
        people = people_count[root]
        if people <= max_people_limit:
             li.append((candy, people))
             
    dp = [0] * K 

    for c, p in li:
        for x in range(max_people_limit, p - 1, -1):
            dp[x] = max(dp[x], dp[x - p] + c)
    
    print(max(dp))
    
if __name__ == '__main__':
    main()
