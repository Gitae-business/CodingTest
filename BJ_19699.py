# 소-난다! https://www.acmicpc.net/problem/19699
from itertools import combinations

def main():
    n, m = map(int, input().split())
    cows = list(map(int, input().split()))

    def IsPrime(num):
        if num < 2: 
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    s = set()
    for c in combinations(cows, m):
        t = sum(c)
        if IsPrime(t):
            s.add(t)

    if not s:
        print(-1)
        return
    
    answer = sorted(s)
    print(*answer)

if __name__ == '__main__':
    main()
