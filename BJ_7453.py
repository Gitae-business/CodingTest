# 합이 0인 네 정수 https://www.acmicpc.net/problem/7453
from collections import Counter

def main():
    n = int(input())
    A, B, C, D = map(list, zip(*(map(int, input().split()) for _ in range(n))))

    ABSum = Counter()
    for a in A:
        for b in B:
            ABSum[a + b] += 1
    
    answer = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in ABSum:
                answer += ABSum[target]
    
    print(answer)

if __name__ == '__main__':
    main()
