# 두 배열의 합 https://www.acmicpc.net/problem/2143
from collections import Counter

def getSub(arr):
    t = []
    l = len(arr)
    for i in range(l):
        total = 0
        for j in range(i, l):
            total += arr[j]
            t.append(total)
    return t

def main():
    T = int(input())

    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    A_sub = getSub(A)
    B_sub = getSub(B)
    B_count = Counter(B_sub)

    ans = 0
    for a in A_sub:
        ans += B_count[T - a]
    print(ans)

if __name__ == '__main__':
    main()
