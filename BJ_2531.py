# 회전 초밥 https://www.acmicpc.net/problem/2531
from collections import defaultdict

def main():
    N, d, k, c = map(int, input().split())
    sushis = [int(input()) for _ in range(N)]
    
    sushis += sushis
    counts = defaultdict(int)
    
    for i in range(k):
        counts[sushis[i]] += 1
    
    current_kinds = len(counts)
    if c not in counts:
        current_kinds += 1
    answer = current_kinds
    
    left_idx = 0
    
    while True:
        counts[sushis[left_idx]] -= 1
        if counts[sushis[left_idx]] == 0:
            del counts[sushis[left_idx]]
        
        left_idx += 1
        right_idx = left_idx + k - 1
        if right_idx >= len(sushis):
            break
        
        counts[sushis[right_idx]] += 1
        
        current_kinds = len(counts)
        if c not in counts:
            current_kinds += 1
        
        answer = max(answer, current_kinds)
        
    print(answer)

if __name__ == '__main__':
    main()