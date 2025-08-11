# 멀티탭 스케줄링 https://www.acmicpc.net/problem/1700
from collections import defaultdict

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    using = set()
    answer = 0
    
    for idx, val in enumerate(arr):
        if val in using:
            continue

        if len(using) < n:
            using.add(val)
            continue
    
        next_use = defaultdict(lambda: float('inf'))
        
        for plugged in using:
            try:
                next_index = arr[idx+1:].index(plugged)
                next_use[plugged] = idx + 1 + next_index
            except ValueError:
                next_use[plugged] = float('inf')
        
        to_unplug = max(using, key=lambda x: next_use[x])
        
        using.remove(to_unplug)
        using.add(val)
        answer += 1
            
    print(answer)

if __name__ == '__main__':
    main()