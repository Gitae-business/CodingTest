# 배열 정렬 https://www.acmicpc.net/problem/28707
import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    arr = tuple(map(int, input().split()))
    M = int(input())
    ops = [list(map(int, input().split())) for _ in range(M)]

    target = tuple(sorted(arr))
    
    dp = {arr: 0}
    pq = [(0, arr)]

    while pq:
        cur_cost, state = heapq.heappop(pq)

        if state == target:
            print(cur_cost)
            return
        
        if dp[state] < cur_cost:
            continue

        for l, r, c in ops:
            new_state = list(state)
            
            new_state[l-1], new_state[r-1] = new_state[r-1], new_state[l-1]
            new_cost = cur_cost + c
            new_state = tuple(new_state)

            if dp.get(new_state, float('inf')) > new_cost:
                dp[new_state] = new_cost
                heapq.heappush(pq, (new_cost, new_state))

    print(-1)

if __name__ == '__main__':
    main()
