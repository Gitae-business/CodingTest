# 트럭 https://www.acmicpc.net/problem/13335
from collections import deque

def main():
    n, w, L = map(int, input().split())
    arr = list(map(int, input().split()))
    
    time = 0
    arrived_trucks_cnt = 0
    left_trucks = deque(arr)
    bridge = deque([0] * w)

    while arrived_trucks_cnt < n:
        time += 1
        arrived = bridge.popleft()
        if arrived > 0:
            arrived_trucks_cnt += 1
        
        if left_trucks and left_trucks[0] + sum(bridge) <= L:
            bridge.append(left_trucks.popleft())
        else:
            bridge.append(0)
    
    print(time)

if __name__ == '__main__':
    main()
