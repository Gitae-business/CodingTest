# 카드 https://www.acmicpc.net/problem/11652
from collections import defaultdict

def main():
    n = int(input())
    cards = defaultdict(int)
    
    for _ in range(n):
        t = int(input())
        cards[t] += 1
    
    mx = max(cards.values())
    candidates = [i for i in cards if cards[i] == mx]
    candidates.sort()
    
    print(candidates[0])   

if __name__ == '__main__':
    main()
