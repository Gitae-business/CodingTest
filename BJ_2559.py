# 수열 https://www.acmicpc.net/problem/2559
import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = arr.copy()

    for i in range(1, N):
        prefix[i] += prefix[i-1]
    
    ans = prefix[K-1]
    for right in range(K, N):
        left = right - K
        ans = max(ans, prefix[right] - prefix[left])

    print(ans)

if __name__ == '__main__':
    main()
